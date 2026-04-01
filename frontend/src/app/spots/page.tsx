import { getSpots } from "@/lib/api";

export default async function SpotsPage() {
  const spots = await getSpots();

  return (
    <section className="section">
      <h2>Shooting Spots</h2>
      <div className="grid">
        {spots.map((spot) => (
          <article className="card" key={spot.id}>
            <strong>{spot.name}</strong>
            <p>
              {spot.prefecture} / {spot.latitude}, {spot.longitude}
            </p>
            <p>{spot.memo}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
