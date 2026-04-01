import { Landmark, Match, SearchRequest, Spot } from "./types";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

async function fetchJson<T>(path: string): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error(`API request failed: ${response.status}`);
  }

  return response.json() as Promise<T>;
}

export async function getSpots(): Promise<Spot[]> {
  return fetchJson<Spot[]>("/api/spots");
}

export async function getLandmarks(): Promise<Landmark[]> {
  return fetchJson<Landmark[]>("/api/landmarks");
}

export async function getMatches(searchRequestId = "search-demo"): Promise<{ items: Match[]; total: number }> {
  return fetchJson<{ items: Match[]; total: number }>(`/api/matches?search_request_id=${searchRequestId}`);
}

export async function getSearch(searchId = "search-demo"): Promise<SearchRequest> {
  return fetchJson<SearchRequest>(`/api/searches/${searchId}`);
}
