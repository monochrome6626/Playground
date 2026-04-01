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

Creates a search request and executes alignment calculation synchronously.

### `GET /api/searches/{search_id}`

Returns current status and search configuration.

### `GET /api/matches?search_request_id=...`

Returns ranked matches for a search request.

### `GET /api/matches/{match_id}`

Returns detailed geometry values for one match.

## API evolution notes

- spots and landmarks endpoints are DB-backed via SQLAlchemy repositories
- searches and matches endpoints are DB-backed in the current iteration
- current search execution is synchronous in the request cycle
- final production flow should enqueue search execution in a background worker
