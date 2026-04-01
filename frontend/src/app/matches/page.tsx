import { MapView } from "@/components/map-view";
import { MatchTable } from "@/components/match-table";
import { getMatches, getSearch } from "@/lib/api";

type MatchesPageProps = {
  searchParams?: Promise<{
    searchId?: string | string[];
  }>;
};

export default async function MatchesPage({ searchParams }: MatchesPageProps) {
  const resolvedSearchParams = (await searchParams) ?? {};
  const searchIdValue = resolvedSearchParams.searchId;
  const searchId = Array.isArray(searchIdValue) ? searchIdValue[0] : searchIdValue;

  if (!searchId) {
    return (
      <section className="section">
        <h2>Search Status</h2>
        <div className="card">
          <p>Create a search from the Search page to view live match results.</p>
        </div>
      </section>
    );
  }

  const [search, matches] = await Promise.all([getSearch(searchId), getMatches(searchId)]);

  return (
    <>
      <section className="section">
        <h2>Search Status</h2>
        <div className="grid">
          <div className="card">
            <div className="label">Status</div>
            <strong>{search.status}</strong>
          </div>
          <div className="card">
            <div className="label">Date Range</div>
            <strong>
              {search.date_from} to {search.date_to}
            </strong>
          </div>
          <div className="card">
            <div className="label">Interval</div>
            <strong>{search.interval_sec} sec</strong>
          </div>
        </div>
      </section>
      <MatchTable matches={matches.items} />
      <MapView />
    </>
  );
}
