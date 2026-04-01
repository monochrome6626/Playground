import Link from "next/link";

import { getMatchDetail } from "@/lib/api";

type MatchDetailPageProps = {
  params: Promise<{
    id: string;
  }>;
  searchParams?: Promise<{
    searchId?: string | string[];
  }>;
};

export default async function MatchDetailPage({ params, searchParams }: MatchDetailPageProps) {
  const { id } = await params;
  const resolvedSearchParams = (await searchParams) ?? {};
  const searchIdValue = resolvedSearchParams.searchId;
  const searchId = Array.isArray(searchIdValue) ? searchIdValue[0] : searchIdValue;

  let detail;
  try {
    detail = await getMatchDetail(id);
  } catch (_error) {
    return (
      <section className="section">
        <h2>Match Detail</h2>
        <div className="card">
          <p>Match was not found.</p>
        </div>
        <div className="actions">
          <Link className="button secondary" href={searchId ? `/matches?searchId=${searchId}` : "/matches"}>
            Back to Matches
          </Link>
        </div>
      </section>
    );
  }

  return (
    <section className="section">
      <h2>Match Detail</h2>
      <div className="grid">
        <div className="card">
          <div className="label">Observed At</div>
          <strong>{new Date(detail.observed_at).toLocaleString("ja-JP")}</strong>
          <p>
            {detail.body} / {detail.event_type}
          </p>
        </div>
        <div className="card">
          <div className="label">Spot / Landmark</div>
          <strong>{detail.spot_name}</strong>
          <p>{detail.landmark_name}</p>
        </div>
        <div className="card">
          <div className="label">Score</div>
          <strong>{detail.score.toFixed(1)}</strong>
          <p>Weather: {detail.weather_summary ?? "n/a"}</p>
        </div>
      </div>

      <div className="grid" style={{ marginTop: 16 }}>
        <div className="card">
          <div className="label">Body Position</div>
          <strong>Azimuth {detail.body_azimuth_deg.toFixed(2)} deg</strong>
          <p>Altitude {detail.body_altitude_deg.toFixed(2)} deg</p>
        </div>
        <div className="card">
          <div className="label">Landmark Position</div>
          <strong>Azimuth {detail.landmark_azimuth_deg.toFixed(2)} deg</strong>
          <p>Altitude {detail.landmark_altitude_deg.toFixed(2)} deg</p>
        </div>
        <div className="card">
          <div className="label">Diff</div>
          <strong>Azimuth {detail.azimuth_diff_deg.toFixed(3)} deg</strong>
          <p>Altitude {detail.altitude_diff_deg.toFixed(3)} deg</p>
        </div>
      </div>

      <div className="actions">
        <Link className="button secondary" href={searchId ? `/matches?searchId=${searchId}` : "/matches"}>
          Back to Matches
        </Link>
      </div>
    </section>
  );
}
