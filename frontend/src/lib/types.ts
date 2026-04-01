export type Spot = {
  id: string;
  name: string;
  latitude: number;
  longitude: number;
  elevation_m?: number | null;
  prefecture?: string | null;
  memo?: string | null;
};

export type Landmark = {
  id: string;
  name: string;
  latitude: number;
  longitude: number;
  base_elevation_m?: number | null;
  height_m: number;
  target_point_type: string;
};

export type SearchRequest = {
  id: string;
  spot_id: string;
  landmark_id: string;
  date_from: string;
  date_to: string;
  body_types: string[];
  event_types: string[];
  azimuth_tolerance_deg: number;
  altitude_tolerance_deg: number;
  interval_sec: number;
  status: string;
};

export type Match = {
  id: string;
  observed_at: string;
  body: string;
  event_type: string;
  score: number;
  azimuth_diff_deg: number;
  altitude_diff_deg: number;
  weather_summary?: string | null;
};
