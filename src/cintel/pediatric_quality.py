"""Run pediatric data quality checks on fictional clinic records."""

import logging
from pathlib import Path

from cintel.utils_clinic import (
    detect_pediatric_quality_issues,
    load_clinic_data,
)

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_ROOT / "data" / "pediatric_quality_data.csv"
OUTPUT_FILE = PROJECT_ROOT / "artifacts" / "pediatric_quality_issues.csv"


def main() -> None:
    """Load pediatric data, identify quality issues, and save results."""
    df = load_clinic_data(DATA_FILE)
    issues = detect_pediatric_quality_issues(df)

    logger.info("Loaded %s pediatric records", df.height)
    logger.info("Records with data quality issues: %s", issues.height)
    logger.info("Records without identified issues: %s", df.height - issues.height)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    issues.write_csv(OUTPUT_FILE)

    logger.info("Saved data quality report: %s", OUTPUT_FILE)
    logger.info("Pediatric data quality validation completed successfully!")


if __name__ == "__main__":
    main()
