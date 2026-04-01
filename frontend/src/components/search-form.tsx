"use client";

import { FormEvent, startTransition, useMemo, useState } from "react";
import { useRouter } from "next/navigation";

import { createSearch } from "@/lib/api";
import { Landmark, SearchRequestCreate, Spot } from "@/lib/types";

type SearchFormProps = {
  spots: Spot[];
  landmarks: Landmark[];
};

export function SearchForm({ spots, landmarks }: SearchFormProps) {
  const router = useRouter();
  const today = useMemo(() => new Date().toISOString().slice(0, 10), []);
  const after30Days = useMemo(() => {
    const d = new Date();
    d.setDate(d.getDate() + 30);
    return d.toISOString().slice(0, 10);
  }, []);

  const [spotId, setSpotId] = useState(spots[0]?.id ?? "");
  const [landmarkId, setLandmarkId] = useState(landmarks[0]?.id ?? "");
  const [dateFrom, setDateFrom] = useState(today);
  const [dateTo, setDateTo] = useState(after30Days);
  const [intervalSec, setIntervalSec] = useState(60);
  const [azimuthTolerance, setAzimuthTolerance] = useState(0.35);
  const [altitudeTolerance, setAltitudeTolerance] = useState(0.35);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  if (spots.length === 0 || landmarks.length === 0) {
    return (
      <section className="section">
        <h2>Search Conditions</h2>
        <div className="card">
          <p>Search needs at least one spot and one landmark. Create a spot first, then try again.</p>
        </div>
      </section>
    );
  }

  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setIsSubmitting(true);
    setError(null);

    const from = new Date(dateFrom);
    const to = new Date(dateTo);
    const rangeDays = Math.floor((to.getTime() - from.getTime()) / (1000 * 60 * 60 * 24));

    if (rangeDays < 0) {
      setError("date_from must be earlier than or equal to date_to.");
      setIsSubmitting(false);
      return;
    }
    if (rangeDays > 366) {
      setError("Date range must be 366 days or fewer.");
      setIsSubmitting(false);
      return;
    }

    const payload: SearchRequestCreate = {
      spot_id: spotId,
      landmark_id: landmarkId,
      date_from: dateFrom,
      date_to: dateTo,
      body_types: ["sun", "moon"],
      event_types: ["sunrise", "sunset", "moonrise", "moonset"],
      azimuth_tolerance_deg: azimuthTolerance,
      altitude_tolerance_deg: altitudeTolerance,
      interval_sec: intervalSec,
    };

    try {
      const created = await createSearch(payload);
      startTransition(() => {
        router.push(`/matches?searchId=${created.id}`);
      });
    } catch (submitError: unknown) {
      const message = submitError instanceof Error ? submitError.message : "Failed to create search request.";
      setError(message);
      setIsSubmitting(false);
    }
  }

  return (
    <section className="section">
      <h2>Search Conditions</h2>
      <form onSubmit={onSubmit}>
        <div className="grid">
          <div className="card">
            <label className="label" htmlFor="spotId">
              Shooting Spot
            </label>
            <select id="spotId" className="input" value={spotId} onChange={(e) => setSpotId(e.target.value)}>
              {spots.map((spot) => (
                <option key={spot.id} value={spot.id}>
                  {spot.name}
                </option>
              ))}
            </select>
          </div>
          <div className="card">
            <label className="label" htmlFor="landmarkId">
              Landmark
            </label>
            <select
              id="landmarkId"
              className="input"
              value={landmarkId}
              onChange={(e) => setLandmarkId(e.target.value)}
            >
              {landmarks.map((landmark) => (
                <option key={landmark.id} value={landmark.id}>
                  {landmark.name}
                </option>
              ))}
            </select>
          </div>
          <div className="card">
            <label className="label" htmlFor="dateFrom">
              Date From
            </label>
            <input id="dateFrom" className="input" type="date" value={dateFrom} onChange={(e) => setDateFrom(e.target.value)} />
          </div>
          <div className="card">
            <label className="label" htmlFor="dateTo">
              Date To
            </label>
            <input id="dateTo" className="input" type="date" value={dateTo} onChange={(e) => setDateTo(e.target.value)} />
          </div>
          <div className="card">
            <label className="label" htmlFor="intervalSec">
              Interval (sec)
            </label>
            <input
              id="intervalSec"
              className="input"
              type="number"
              min={10}
              max={3600}
              step={10}
              value={intervalSec}
              onChange={(e) => setIntervalSec(Number(e.target.value))}
            />
            <p>10-3600 seconds</p>
          </div>
          <div className="card">
            <label className="label" htmlFor="azTol">
              Azimuth Tolerance (deg)
            </label>
            <input
              id="azTol"
              className="input"
              type="number"
              min={0.01}
              max={180}
              step={0.01}
              value={azimuthTolerance}
              onChange={(e) => setAzimuthTolerance(Number(e.target.value))}
            />
            <p>0.01-180 degrees</p>
          </div>
          <div className="card">
            <label className="label" htmlFor="altTol">
              Altitude Tolerance (deg)
            </label>
            <input
              id="altTol"
              className="input"
              type="number"
              min={0.01}
              max={90}
              step={0.01}
              value={altitudeTolerance}
              onChange={(e) => setAltitudeTolerance(Number(e.target.value))}
            />
            <p>0.01-90 degrees</p>
          </div>
        </div>
        <div className="actions">
          <button className="button" type="submit" disabled={isSubmitting}>
            {isSubmitting ? "Searching..." : "Run Search"}
          </button>
        </div>
      </form>
      {error ? <p>{error}</p> : null}
    </section>
  );
}
