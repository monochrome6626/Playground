# Operations

## Development workflow

- create features in small vertical slices
- keep astronomy logic covered with unit tests
- document API and schema changes in the same branch

## Data management

- landmarks should be seeded from source-controlled fixtures
- spots can be user-generated
- weather data should be cached with fetch timestamps

## Future production concerns

- separate API and worker processes
- enable structured logging
- add retry rules around external weather APIs
- back up PostgreSQL regularly
