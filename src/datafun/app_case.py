"""
src/datafun/app_case.py - Project script (example).

Author: Denise Case
Date: 2026-05
"""

# === IMPORTS ===

import statistics
from typing import Final

from datafun.shared_utils import setup_logging

LOG = setup_logging()

# === GLOBAL CONSTANTS ===

COURSE_NAME: Final[str] = "Data Analytics Fundamentals"
COURSE_NUMBER: Final[int] = 608
COURSE_HOURS_PER_WEEK: Final[float] = 20.0
ASSUMES_PRIOR_EXPERIENCE: Final[bool] = False
USES_PROFESSIONAL_PYTHON: Final[bool] = True
HELPFUL_TRAITS: Final[list[str]] = [
    "patience",
    "curiosity",
    "humor",
    "tenacity",
]

# === SUMMARY FUNCTION ===

def get_summary() -> str:
    summary: str = f"""
    Course Information:
        Course name: {COURSE_NAME}
        Course number: {COURSE_NUMBER}
        Course hrs/wk: {COURSE_HOURS_PER_WEEK:.2f}
        Assumes prior experience: {ASSUMES_PRIOR_EXPERIENCE}
        Uses Professional Python: {USES_PROFESSIONAL_PYTHON}
        Helpful traits: {HELPFUL_TRAITS}
    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    return summary

# === STATISTICS FUNCTION ===

def get_statistics() -> str:
    snowfall_inches: list[float] = [2.5, 3.5, 4.5, 5.5, 6.5]

    total: float = sum(snowfall_inches)
    count: int = len(snowfall_inches)
    minimum: float = min(snowfall_inches)
    maximum: float = max(snowfall_inches)
    average: float = statistics.mean(snowfall_inches)
    std_dev: float = statistics.stdev(snowfall_inches)

    summary: str = f"""
    Descriptive Statistics for Snowfall (inches):
        Total snowfall: {total:.2f} inches
        Count of measurements: {count}
        Minimum snowfall: {minimum:.2f} inches
        Maximum snowfall: {maximum:.2f} inches
        Average snowfall: {average:.2f} inches
        Standard deviation: {std_dev:.2f} inches
    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    return summary

# === MAIN FUNCTION ===

def main() -> None:
    LOG.info("=== START Example Script ===")

    LOG.info(get_summary())
    LOG.info(get_statistics())

    LOG.info("=== END Example Script ===")

# === EXECUTION GUARD ===

if __name__ == "__main__":
    main()
