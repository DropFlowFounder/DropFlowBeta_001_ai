from typing import Dict, Any
from datetime import datetime


def validate_url(url: str) -> bool:
    """Validate if a string is a proper URL"""
    from urllib.parse import urlparse
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def format_currency(amount: float) -> str:
    """Format currency amount with 2 decimal places"""
    return f"{amount:.2f}"


def get_current_timestamp() -> str:
    """Get current timestamp in ISO format"""
    return datetime.utcnow().isoformat()


def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text to specified length with ellipsis if needed"""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."


def create_unique_link(traffic_id: int, task_id: int) -> str:
    """Create a unique tracking link for an assignment"""
    return f"https://traffk.example.com/r?r={traffic_id}_{task_id}"