"""Helper utility functions."""

import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


def safe_get(data: Dict[str, Any], key: str, default: Any = None) -> Any:
    """Safely get value from dictionary.

    Args:
        data: Dictionary to get from
        key: Key to retrieve
        default: Default value if key not found

    Returns:
        Value from dictionary or default
    """
    return data.get(key, default)


def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text to maximum length.

    Args:
        text: Text to truncate
        max_length: Maximum length

    Returns:
        Truncated text with ellipsis if needed
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."
