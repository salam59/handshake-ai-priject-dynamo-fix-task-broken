import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_exists():
    """The agent produced a report file."""
    assert REPORT.exists(), "no report.json found"


def test_report_valid_json():
    """The report file contains valid JSON."""
    data = json.loads(REPORT.read_text())
    assert isinstance(data, dict), "report.json root must be a JSON object"


def test_total_requests():
    """total_requests equals the number of log lines."""
    data = json.loads(REPORT.read_text())
    assert data.get("total_requests") == 6, (
        f"expected total_requests=6, got {data.get('total_requests')}"
    )


def test_unique_ips():
    """unique_ips equals the number of distinct client IPs."""
    data = json.loads(REPORT.read_text())
    assert data.get("unique_ips") == 3, (
        f"expected unique_ips=3, got {data.get('unique_ips')}"
    )


def test_top_path():
    """top_path is the most frequently requested path."""
    data = json.loads(REPORT.read_text())
    assert data.get("top_path") == "/index.html", (
        f"expected top_path='/index.html', got {data.get('top_path')}"
    )
