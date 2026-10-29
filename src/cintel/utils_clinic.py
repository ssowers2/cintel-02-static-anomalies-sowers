"""utils_clinic.py.

Author: Sabriya Sowers
Date: 2026-10-25

Shared helper functions for the clinic anomaly-detection domain.

Used by:
- src/cintel/anomaly_detector.py (cintel-02)
- app.py

"""

from pathlib import Path

import polars as pl


def load_clinic_data(data_file: Path) -> pl.DataFrame:
    """Read pediatric clinic age/height records from a CSV file."""
    return pl.read_csv(data_file)


def detect_clinic_anomalies(
    df: pl.DataFrame,
    max_age_years: float,
    max_height_inches: float,
) -> pl.DataFrame:
    """Return rows meeting one or more defined anomaly threshold conditions."""
    return df.filter(
        (pl.col("age_years") >= max_age_years)
        | (pl.col("height_inches") >= max_height_inches)
    )


def detect_pediatric_quality_issues(df: pl.DataFrame) -> pl.DataFrame:
    """Identifies pediatric records with missing or invalid values."""
    return df.with_columns(
        pl.when(pl.col("age_years").is_null())
        .then(pl.lit("Missing age"))
        .when(pl.col("height_inches").is_null())
        .then(pl.lit("Missing height"))
        .when(pl.col("age_years") < 0)
        .then(pl.lit("Negative age"))
        .when(pl.col("height_inches") < 0)
        .then(pl.lit("Negative height"))
        .when(pl.col("height_inches") == 0)
        .then(pl.lit("Zero height"))
        .otherwise(pl.lit(None, dtype=pl.String))
        .alias("quality_issue")
    ).filter(pl.col("quality_issue").is_not_null())
