import Link from "next/link";

import { Match } from "@/lib/types";

type MatchTableProps = {
  matches: Match[];
  searchId: string;
};

export function MatchTable({ matches, searchId }: MatchTableProps) {
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
            <th>Detail</th>
          </tr>
        </thead>
        <tbody>
          {matches.length === 0 ? (
            <tr>
              <td colSpan={7}>No matches found for the selected conditions.</td>
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
              <td>
                <Link className="button secondary" href={`/matches/${match.id}?searchId=${searchId}`}>
                  View
                </Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}
