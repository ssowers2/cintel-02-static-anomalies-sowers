# Apply Ideas

Technique: Detect values outside a reasonable range using simple domain thresholds.

In this module, anomalies are defined using domain knowledge rather than advanced statistical methods.

A good dataset for this module:

- contains measurements of a real-world system
- has clearly defined units
- allows you to define reasonable maximum or minimum values

## Example Systems

### Animal Measurements

Possible fields:

- age
- weight
- height

Questions to explore:

- What values clearly violate biological limits?
- Are there cases that seem unusual but still possible?
- How does domain knowledge affect threshold selection?

### Vehicle Speeds

Possible fields:

- speed_mph
- vehicle_type
- location

Questions to explore:

- What speeds are clearly impossible or unsafe?
- Should thresholds vary by vehicle type?

### Building Temperatures

Possible fields:

- indoor_temperature
- outdoor_temperature

Questions to explore:

- What temperature values suggest a sensor error?
- What values suggest a system malfunction?

### Product Prices

Possible fields:

- product_price
- category

Questions to explore:

- What price values are clearly incorrect?
- Are there extreme values that require investigation?

### Network Response Times

Possible fields:

- latency_ms
- request_size

Questions to explore:

- What latency values indicate a problem?
- How might thresholds vary across systems?
