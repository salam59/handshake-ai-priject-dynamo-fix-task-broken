# Access-Log Report

An Apache-style access log is located at `/app/access.log`.
Parse it and produce a JSON report saved to `/app/report.json`.

## Success criteria

1. The output file **`/app/report.json`** exists and contains valid JSON.
2. The JSON object has a key **`total_requests`** (integer) — the total number of log lines (requests).
3. The JSON object has a key **`unique_ips`** (integer) — the count of distinct client IP addresses.
4. The JSON object has a key **`top_path`** (string) — the request path that appears most frequently.
