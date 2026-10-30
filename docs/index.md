# Static Anomaly Detection

Continuous Intelligence | Project 02 | Example Report

## Overview

This project investigates how simple domain thresholds
can identify unusual observations in static tabular data.

The example analyzes pediatric clinic records to identify
ages and heights outside defined upper limits.

## Data

The dataset contains 22 patient observations with:

- `age_years` - patient age in years.
- `height_inches` - patient height in inches.

[View Example Dataset](https://github.com/denisecase/cintel-02-static-anomalies/blob/main/data/clinic_data.csv)

## Original Example Methods

The pipeline uses Python and Polars to read the data
and identify observations meeting either condition:

- Age greater than or equal to 16 years.
- Height greater than or equal to 72 inches.

These are example screening rules, not clinical standards.

Records meeting either condition are saved as anomalies.

## Original Example Results

The example pipeline identified **3 anomalous records**.

| Age (years) | Height (inches) | Reason           |
| ----------- | --------------- | ---------------- |
| 12          | 95              | Height threshold |
| 10          | 72              | Height threshold |
| 120         | 66              | Age threshold    |

[View Anomaly Results](https://github.com/denisecase/cintel-02-static-anomalies/blob/main/artifacts/anomalies.csv)

## Interpretation

The results demonstrate that threshold-based detection
can identify observations requiring further investigation.

The records do not necessarily indicate incorrect data.
They identify values that warrant review.

For example, the recorded age of 120 years suggests
a possible data-entry or population-classification issue.

## Limitations

The current rules detect only values exceeding upper limits.

Unusually small measurements, such as a height of 5 inches
for an eight-year-old, are not detected.

A stronger approach would consider lower limits,
age-dependent expectations, and domain knowledge.

## Conclusion

Static anomaly detection provides a simple,
interpretable approach for screening observations.

The same principles can be applied repeatedly as
new observations arrive in a monitoring system.

## Documentation Index

- **Home** - this landing page
- [**Project Instructions**](project-instructions.md)
- [**Glossary**](glossary.md)
- [**API**](api.md)
- [**Reactive App**](./app/index.html)

## Project Links

- [GitHub Repository](https://github.com/ssowers2/cintel-02-static-anomalies-sowers)
- [My Anomaly Detection Pipeline](https://github.com/ssowers2/cintel-02-static-anomalies-sowers/blob/main/src/cintel/anomaly_detector.py)
- [My Results and Artifacts](https://github.com/ssowers2/cintel-02-static-anomalies-sowers/tree/main/artifacts)

## Project Resources

- [Project Instructions](project-instructions.md)
- [Professional Python Guide](https://denisecase.github.io/pro-analytics-02/)
- [Professional Python Project Explainer](https://pup-pack.github.io/professional-python-project-explainer/).
- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)

## Custom Modifications

### Experiment 1: Adjusting the Height Threshold

**Modification:** Changed the height threshold from 72 inches to 70 inches in `src/cintel/anomaly_detector.py`.

**Reason:** I wanted to see how changing a predefined threshold would affect the number of anomalies identified.

**Prediction:** If I lowered the height threshold from 72 to 70 inches, I expected the program to identify four anomalies instead of three because an additional record would meet the new threshold.

**Results:** After running the pipeline, the program identified four anomalies out of 22 patient records, compared to three with the original threshold.

**What I Learned:** Even a small adjustment to a threshold can change which records are flagged for review. This demonstrates why data quality rules and thresholds should be carefully defined and documented.

### Experiment Results Comparison

| Measurement | Original | Modified |
|---|---|---|
| Height threshold | 72 inches | 70 inches |
| Age threshold | 16 years | 16 years |
| Patient records | 22 | 22 |
| Anomalies identified | 3 | 4 |

Lowering the height threshold identified one additional record, demonstrating how changes to screening rules can affect the number of records flagged for review.

### Custom Application: Pediatric Data Quality Validation

This application uses Python and Polars to identify missing or invalid values in fictional pediatric patient records. Unlike the original example, which focuses on measurements exceeding upper thresholds, this project examines data completeness and validity. The goal is to demonstrate how automated validation checks can identify records that may need correction or further review.

#### Dataset and Validation Methods

I created a synthetic dataset containing 50 fictional pediatric patient records. Each record includes two fields: `age_years` and `height_inches`.

Using Python and Polars, I developed validation rules to identify five types of data quality issues:

- Missing age
- Missing height
- Negative age
- Negative height
- Zero height

These rules focus on data completeness and basic validity rather than clinical diagnosis. The application saves flagged records to `artifacts/pediatric_quality_issues.csv`.

#### Validation Results

The application analyzed 50 records and identified 13 records requiring review. The remaining 37 records passed the defined validation checks.

| Data Quality Issue | Records Flagged |
|---|---:|
| Missing age | 4 |
| Missing height | 3 |
| Negative age | 3 |
| Negative height | 2 |
| Zero height | 1 |
| **Total** | **13** |

Overall, **74% of records passed** the validation checks, while **26% were flagged for review**.

The results demonstrate how automated data quality checks can help identify incomplete or invalid records before they are used for reporting and analysis.

Because this is a fictional dataset, no real patient information or protected health information (PHI) was used.

#### Limitations

The application checks five basic data quality conditions. It does not evaluate age-specific height expectations or other clinical plausibility rules. Each flagged record is assigned its first detected issue, so additional issues in the same record may not be displayed.

#### Interactive Pediatric Data Quality Dashboard

The dashboard below summarizes the results of the pediatric data quality validation process. It displays the total records analyzed, records that passed validation, records flagged for review, and the frequency of each data quality issue.

<iframe
    src="assets/pediatric_dashboard.html"
    width="100%"
    height="850"
    title="Interactive Pediatric Data Quality Dashboard"
    style="border: none;"
></iframe>
