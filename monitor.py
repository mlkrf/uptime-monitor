import time
from datetime import datetime

import requests

DEFAULT_URLS = [
    "https://www.google.com",
    "https://github.com",
]

def check_site(url):
    started = time.perf_counter()

    try:
        response = requests.get(url, timeout=5)
        elapsed_ms = (time.perf_counter() - started) * 1000
        return {
            "url": url,
            "status": response.status_code,
            "online": response.ok,
            "response_ms": round(elapsed_ms, 2),
            "checked_at": datetime.now().isoformat(timespec="seconds"),
        }
    except requests.RequestException as exc:
        return {
            "url": url,
            "status": None,
            "online": False,
            "response_ms": None,
            "checked_at": datetime.now().isoformat(timespec="seconds"),
            "error": str(exc),
        }

def main():
    print("Simple Uptime Monitor")
    print("Press Enter to use the default websites.")
    user_input = input("URLs separated by commas: ").strip()

    urls = (
        [url.strip() for url in user_input.split(",") if url.strip()]
        if user_input
        else DEFAULT_URLS
    )

    print()
    for url in urls:
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        result = check_site(url)

        state = "ONLINE" if result["online"] else "OFFLINE"
        latency = (
            f'{result["response_ms"]} ms'
            if result["response_ms"] is not None
            else "N/A"
        )

        print(
            f'{state:7} | {result["url"]} | '
            f'Status: {result["status"]} | Response: {latency}'
        )

        if "error" in result:
            print(f'         Error: {result["error"]}')

if __name__ == "__main__":
    main()
