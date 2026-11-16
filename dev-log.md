# Dev Log

## Up to 16 November

### What confused me

- How to send HTTP requests and pass data to POST, DELETE, and other calls.
- How parameterized SQL queries work, especially the `?` placeholders and the values passed to `cur.execute()`.

### Mistake I found

- I did not treat task IDs as strings from the start. This caused issues with IDs like `0001` and `1`.

### What to study

- HTTP requests and computer networks.
- Parameterized SQL queries.

### Next steps

- Generate UUIDs for tasks.
- Add optional filters.
- Try idempotency keys for POST requests to avoid creating duplicate tasks when a request is retried.
