import { Landmark, Match, MatchDetail, SearchRequest, SearchRequestCreate, Spot } from "./types";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

async function extractErrorMessage(response: Response): Promise<string> {
  try {
    const payload = (await response.json()) as { detail?: unknown };
    if (typeof payload.detail === "string") {
      return payload.detail;
    }
    if (Array.isArray(payload.detail) && payload.detail.length > 0) {
      const first = payload.detail[0] as { msg?: string };
      if (typeof first?.msg === "string") {
        return first.msg;
      }
    }
  } catch (_error) {
    // fall back to generic message
  }
  return `API request failed: ${response.status}`;
}

async function fetchJson<T>(path: string): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error(await extractErrorMessage(response));
  }

  return response.json() as Promise<T>;
}

async function postJson<T>(path: string, payload: unknown): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error(await extractErrorMessage(response));
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

export async function createSearch(payload: SearchRequestCreate): Promise<SearchRequest> {
  return postJson<SearchRequest>("/api/searches", payload);
}

export async function getMatchDetail(matchId: string): Promise<MatchDetail> {
  return fetchJson<MatchDetail>(`/api/matches/${matchId}`);
}
