# Requirements

## Functional requirements

1. Users can register and view shooting spots in the Kanto region.
2. Users can search for alignments against Tokyo Skytree and Tokyo Tower.
3. Users can search around sunrise, sunset, moonrise, and moonset.
4. The system returns ranked candidate timestamps with score and delta values.
5. Users can inspect each match in a detail view.

## Non-functional requirements

- search orchestration should separate request handling from heavy calculation
- astronomy logic should be testable independently from the API
- the MVP should run locally with Docker and PostgreSQL
- APIs should stay stable enough for a future mobile client

## Match definition

- `azimuth_diff_deg`: angular difference in horizontal direction between the celestial body and the target landmark point
- `altitude_diff_deg`: angular difference in vertical direction between the celestial body and the target landmark point
- `score`: weighted closeness metric derived from both deltas

## Explicit MVP assumptions

- the first release computes theoretical visibility only
- terrain and building occlusion are not considered
- weather is informative only and does not block candidate generation
- all timestamps are stored in timezone-aware form and shown in Japan Standard Time by default
