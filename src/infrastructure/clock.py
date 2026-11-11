"""! @file clock.py
@brief System clock adapter.
"""
from datetime import date

from constants import POST_DATE_FORMAT


class SystemClock:
    """! @brief Supplies today's date from the operating system."""

    def today(self) -> str:
        """! @brief Returns today's date formatted for display."""
        return date.today().strftime(POST_DATE_FORMAT)
