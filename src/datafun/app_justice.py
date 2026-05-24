"""
src/datafun/app_justice.py - Justice's Project Script

Author: Justice Tefera
Date: 2026-05

This script mirrors the instructor's example (app_case.py) but uses
Justice's own variables, summary, and descriptive statistics.
"""

# === IMPORTS ===

import statistics
from typing import Final

from datafun.shared_utils import setup_logging

LOG = setup_logging()

# === CONFIGURE LOGGER ===

LOG = setup_logging()

# === GLOBAL CONSTANTS (YOUR VERSION) ===

IS_VETERAN: Final[bool] = True
YEAR_STARTING_GRAD_SCHOOL: Final[int] = 2026
HOURS_PER_WEEK_STUDY: Final[float] = 18.5
CITY: Final[str] = "Berlin"
ANALYTIC_SPECIALTY: Final[str] = "Data Ethics & Quantitative Reasoning"

SKILLS: Final[list[str]] = [
    "Python",
    "Git",
    "Statistics",
    "Automation",
    "Teaching",
]

# === SUMMARY FUNCTION ===

def get_summary() -> str:
    """Return a formatted summary of Justice's profile."""
    summary: str = f"""
    Justice's Profile Summary:
        Veteran: {IS_VETERAN}
        Grad School Start Year: {YEAR_STARTING_GRAD_SCHOOL}
        Study Hours/Week: {HOURS_PER_WEEK_STUDY:.2f}
        City: {CITY}
        Specialty: {ANALYTIC_SPECIALTY}
        Skills: {SKILLS}
    """

    LOG.info("Generated Justice's summary string.")
    return summary

# === STATISTICS FUNCTION ===

def get_statistics() -> str:
    """Return descriptive statistics for weekly study hours."""

    study_hours: list[float] = [12.0, 15.5, 18.5, 20.0, 17.0]

    total: float = sum(study_hours)
    count: int = len(study_hours)

    minimum: float = min(study_hours) if count > 0 else 0.0
    maximum: float = max(study_hours) if count > 0 else 0.0
    average: float = statistics.mean(study_hours) if count > 0 else 0.0
    std_dev: float = statistics.stdev(study_hours) if count > 1 else 0.0

    summary: str = (
        f"\n"
        f"    Descriptive Statistics for Weekly Study Hours:\n"
        f"        Total hours: {total:.2f}\n"
        f"        Number of weeks: {count}\n"
        f"        Minimum hours: {minimum:.2f}\n"
        f"        Maximum hours: {maximum:.2f}\n"
        f"        Average hours: {average:.2f}\n"
        f"        Standard deviation: {std_dev:.2f}\n"
    )

    LOG.info("Generated Justice's statistics string.")
    return summary

# === MAIN FUNCTION ===

def main() -> None:
    """Entry point when running this file as a Python script."""

    LOG.info("=== START Justice's Script ===")

    summary: str = get_summary()
    LOG.info(summary)

    stats: str = get_statistics()
    LOG.info(stats)

    LOG.info("=== END Justice's Script ===")

if __name__ == "__main__":
    main()
