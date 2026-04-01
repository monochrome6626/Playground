import { Landmark, Spot } from "@/lib/types";

type SearchFormProps = {
  spots: Spot[];
  landmarks: Landmark[];
};

export function SearchForm({ spots, landmarks }: SearchFormProps) {
  return (
    <section className="section">
      <h2>Search Conditions</h2>
      <div className="grid">
        <div className="card">
          <div className="label">Shooting Spot</div>
          <strong>{spots[0]?.name ?? "No spot yet"}</strong>
          <p>Initial scaffold keeps this read-only until the create flow is added.</p>
        </div>
        <div className="card">
          <div className="label">Landmark</div>
          <strong>{landmarks.map((item) => item.name).join(" / ")}</strong>
          <p>Tokyo Skytree and Tokyo Tower are seeded as the first managed landmarks.</p>
        </div>
        <div className="card">
          <div className="label">Events</div>
          <strong>Sunrise / Sunset / Moonrise / Moonset</strong>
          <p>Alignment windows will be searched around each event instead of over the whole day.</p>
        </div>
      </div>
      <div className="actions">
        <span className="button">Search API wiring next</span>
      </div>
    </section>
  );
}
