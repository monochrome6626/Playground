# Schema

## Core tables

### `spots`

- `id` string primary key
- `name` string
- `latitude` double precision
- `longitude` double precision
- `elevation_m` double precision nullable
- `prefecture` string nullable
- `memo` text nullable

### `landmarks`

- `id` string primary key
- `name` string
- `latitude` double precision
- `longitude` double precision
- `base_elevation_m` double precision nullable
- `height_m` double precision
- `target_point_type` string

### `search_requests`

- `id` string primary key
- `spot_id` string
- `landmark_id` string
- `date_from` date
- `date_to` date
- `body_types` json
- `event_types` json
- `azimuth_tolerance_deg` double precision
- `altitude_tolerance_deg` double precision
- `interval_sec` integer
- `status` string

### `matches`

- `id` string primary key
- `search_request_id` string
- `spot_id` string
- `landmark_id` string
- `body` string
- `event_type` string
- `observed_at` timestamptz
- `azimuth_diff_deg` double precision
- `altitude_diff_deg` double precision
- `score` double precision

## Migration roadmap

1. create the four core tables
2. add audit timestamps
3. add weather cache and saved searches
4. add PostGIS geometry columns
