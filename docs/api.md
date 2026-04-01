# API

## Endpoints

### `GET /health`

Returns service availability.

### `GET /api/spots`

Returns registered shooting spots.

### `POST /api/spots`

Creates a new shooting spot.

### `GET /api/landmarks`

Returns managed landmarks.

### `POST /api/searches`

Creates a search request and queues the alignment calculation.

### `GET /api/searches/{search_id}`

Returns current status and search configuration.

### `GET /api/matches?search_request_id=...`

Returns ranked matches for a search request.

### `GET /api/matches/{match_id}`

Returns detailed geometry values for one match.

## API evolution notes

- current scaffold returns fixtures so the frontend can be built in parallel
- next step is replacing fixtures with repository-backed handlers
- final search flow should enqueue work instead of calculating inside the request cycle
