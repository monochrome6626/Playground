import { Match } from "@/lib/types";

type MatchTableProps = {
  matches: Match[];
};

export function MatchTable({ matches }: MatchTableProps) {
  return (
    <section className="section">
      <h2>Candidate Matches</h2>
      <table className="table">
        <thead>
          <tr>
            <th>Date/Time</th>
            <th>Body</th>
            <th>Event</th>
            <th>Score</th>
            <th>Azimuth Diff</th>
            <th>Altitude Diff</th>
          </tr>
        </thead>
        <tbody>
          {matches.length === 0 ? (
            <tr>
              <td colSpan={6}>No matches found for the selected conditions.</td>
            </tr>
          ) : null}
          {matches.map((match) => (
            <tr key={match.id}>
              <td>{new Date(match.observed_at).toLocaleString("ja-JP")}</td>
              <td>{match.body}</td>
              <td>{match.event_type}</td>
              <td>{match.score.toFixed(1)}</td>
              <td>{match.azimuth_diff_deg.toFixed(2)} deg</td>
              <td>{match.altitude_diff_deg.toFixed(2)} deg</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}
