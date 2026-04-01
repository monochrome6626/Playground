import Link from "next/link";

export default function HomePage() {
  return (
    <>
      <section className="hero">
        <span className="pill">MVP scaffold</span>
        <h1>AstroShot Planner</h1>
        <p>
          Find candidate moments in the Kanto region when the sun or moon aligns with Tokyo Skytree or Tokyo Tower for
          telephoto photography.
        </p>
        <div className="actions">
          <Link className="button" href="/search">
            Open Search Workspace
          </Link>
          <Link className="button secondary" href="/matches">
            Review Demo Results
          </Link>
        </div>
      </section>

      <section className="section">
        <h2>First Milestone</h2>
        <div className="grid">
          <div className="card">
            <strong>Search windows</strong>
            <p>Restrict calculations to sunrise, sunset, moonrise, and moonset windows for practical performance.</p>
          </div>
          <div className="card">
            <strong>Alignment scoring</strong>
            <p>Rank candidates by azimuth and altitude difference so photographers can focus on the closest shots.</p>
          </div>
          <div className="card">
            <strong>Reusable spots</strong>
            <p>Save recurring shooting locations across the Kanto region and compare results between landmarks.</p>
          </div>
        </div>
      </section>
    </>
  );
}
