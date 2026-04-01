import { MapView } from "@/components/map-view";
import { MatchTable } from "@/components/match-table";
import { getMatches, getSearch } from "@/lib/api";

export default async function MatchesPage() {
  const [search, matches] = await Promise.all([getSearch(), getMatches()]);

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
