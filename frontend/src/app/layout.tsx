import "./globals.css";
import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "AstroShot Planner",
  description: "Plan sunrise, sunset, moonrise, and moonset alignment shots with Tokyo landmarks.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="ja">
      <body>
        <main>
          <div className="shell">
            <nav className="actions" aria-label="Primary">
              <Link className="button secondary" href="/">
                Home
              </Link>
              <Link className="button secondary" href="/search">
                Search
              </Link>
              <Link className="button secondary" href="/matches">
                Matches
              </Link>
              <Link className="button secondary" href="/spots">
                Spots
              </Link>
            </nav>
            {children}
          </div>
        </main>
      </body>
    </html>
  );
}
