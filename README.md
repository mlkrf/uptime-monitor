# Uptime Monitor

A small Python networking utility that checks whether websites are reachable and measures their response time.

## Features

- Check multiple websites in one run
- Display HTTP status codes
- Measure response time in milliseconds
- Handle timeouts and connection errors
- Accept custom URLs from the user

## Tech

- Python
- Requests
- HTTP

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python monitor.py
```

## What I learned

This project helped me practise HTTP requests, exception handling, timing operations, and working with real network responses.

## Possible improvements

- Run checks automatically every few minutes
- Save results to CSV or SQLite
- Send an alert when a site goes offline
- Build a dashboard showing uptime history
