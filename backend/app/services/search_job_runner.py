from concurrent.futures import Future, ThreadPoolExecutor
from threading import Lock

from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.core.db import SessionLocal
from app.repositories.match_repository import MatchRepository
from app.repositories.search_request_repository import SearchRequestRepository
from app.services.search_service import SearchService


class SearchJobRunner:
    def __init__(self, *, max_workers: int, session_factory: sessionmaker) -> None:
        self._executor = ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="search-worker")
        self._session_factory = session_factory
        self._search_repository = SearchRequestRepository()
        self._match_repository = MatchRepository()
        self._search_service = SearchService()
        self._lock = Lock()
        self._futures: dict[str, Future[None]] = {}

    def configure_session_factory(self, session_factory: sessionmaker) -> None:
        self._session_factory = session_factory

    def enqueue(self, search_id: str) -> None:
        with self._lock:
            existing = self._futures.get(search_id)
            if existing is not None and not existing.done():
                return
            self._futures[search_id] = self._executor.submit(self._run, search_id)

    def wait(self, search_id: str, timeout: float | None = None) -> None:
        with self._lock:
            future = self._futures.get(search_id)
        if future is None:
            return
        future.result(timeout=timeout)

    def shutdown(self) -> None:
        self._executor.shutdown(wait=False, cancel_futures=False)

    def _run(self, search_id: str) -> None:
        with self._session_factory() as db:
            record = self._search_repository.set_status(db, search_id, "processing")
            if record is None:
                return

            try:
                matches = self._search_service.generate_matches(db, record)
                self._match_repository.replace_for_search(db, search_request_id=search_id, matches=matches)
                self._search_repository.set_status(db, search_id, "completed")
            except Exception:
                self._search_repository.set_status(db, search_id, "failed")


search_job_runner = SearchJobRunner(
    max_workers=max(settings.search_worker_count, 1),
    session_factory=SessionLocal,
)
