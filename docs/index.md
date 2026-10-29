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

| Measurement | Original Ex | Modified Experiment |
|---|---|---|
| Height threshold | 72 inches | 70 inches |
| Age threshold | 16 years | 16 years |
| Patient records | 22 | 22 |
| Anomalies identified | 3 | 4 |

Lowering the height threshold identified one additional record, demonstrating how changes to screening rules can affect the number of records flagged for review.
