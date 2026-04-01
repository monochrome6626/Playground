# Worker Notes

This directory is reserved for background search jobs such as:

- precomputing alignment candidates
- refreshing weather cache
- regenerating ephemeris-heavy results

The initial scaffold keeps batch execution inside the backend plan until the search volume justifies a dedicated worker process.
