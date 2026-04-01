# Algorithm

## Search strategy

The application should search only around sunrise, sunset, moonrise, and moonset windows rather than sampling every minute of every day.

## Planned flow

1. Generate relevant event windows for each day in the requested range.
2. Sample timestamps inside each window using `interval_sec`.
3. For each timestamp:
   - compute sun or moon azimuth and altitude at the shooting spot
   - compute landmark azimuth and apparent altitude from the same spot
   - calculate angular deltas
   - score the candidate
4. Persist candidates that fall inside the configured tolerances.

## Scoring

The current scaffold uses a placeholder linear score.

Future improvements:

- weight azimuth more heavily than altitude when photographers care about side-to-side overlap
- include moon illumination
- include atmospheric extinction near the horizon
- adjust rankings using forecast cloud cover
