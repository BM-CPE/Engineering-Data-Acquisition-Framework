# EDAF — Engineering Data Acquisition Framework

## Overview

**EDAF (Engineering Data Acquisition Framework)** is a Python-based engineering software project designed to collect, validate, display, and log sensor measurement data.

The framework simulates an engineering data-acquisition workflow using pressure, temperature, and flow-rate measurements. It applies validation rules to determine whether measurements fall within acceptable operating ranges, generates PASS/FAIL status results, and stores valid measurement data in a timestamped CSV log.

The goal of EDAF is to demonstrate how Python can be used to organize engineering measurement data, perform validation, and create a scalable foundation for future data-acquisition and instrumentation applications.

---

## Key Features

- Accepts pressure, temperature, and flow-rate measurements
- Validates user input before processing
- Applies defined operating limits to each sensor measurement
- Generates PASS/FAIL status results
- Prevents invalid measurements from being logged
- Adds timestamps to measurement records
- Stores measurement data in CSV format
- Displays formatted engineering measurement reports
- Uses modular Python files to separate major program functions
- Provides a foundation for future sensor, plotting, reporting, and DAQ expansion

---

## Technologies Used

- Python
- CSV file handling
- Python dictionaries
- Functions and modular programming
- Exception handling
- Input validation
- Date and time handling
- Engineering measurement validation
- Sensor data organization

---

## Measurement Types

EDAF currently processes three engineering measurements:

### Pressure

```text
Valid Range: 0–300 psi
```

### Temperature

```text
Valid Range: -50–200 °C
```

### Flow Rate

```text
Valid Range: 0–10
```

Each measurement is evaluated against its defined operating range before being approved for logging.

---

## Project Structure

EDAF separates major program responsibilities into individual modules to improve readability and maintainability.

### `main.py`

Controls the overall program workflow and coordinates user input, validation, reporting, and data logging.

### `utils.py`

Contains reusable utility functions such as numeric input validation.

Example functionality:

```python
get_float()
```

This function ensures that sensor measurements are entered in a valid numeric format before the program continues.

### `validation.py`

Contains sensor validation logic for measurements such as:

```python
validate_pressure()
validate_temperature()
validate_flow_rate()
```

The validation system determines whether each sensor reading falls within its defined operating range.

### `displayData.py`

Formats and displays the engineering measurement report, including:

- Timestamp
- Sensor name
- Measurement value
- Engineering units
- PASS/FAIL status

### `sensor_logger.py`

Handles CSV data logging and stores validated measurements for future analysis.

---

## Example Workflow

EDAF follows a workflow similar to:

```text
Sensor Measurement Input
          ↓
Numeric Input Validation
          ↓
Measurement Range Validation
          ↓
PASS / FAIL Determination
          ↓
Formatted Engineering Report
          ↓
CSV Data Logging
```

Only measurements that satisfy the required validation conditions are approved for logging.

---

## Data Structure

Measurement information is organized using nested Python dictionaries.

Example:

```python
measurement = {
    "Timestamp": "2026-07-17 03:03:31",

    "Pressure_Sensor": {
        "Reading": 124.2,
        "Valid": True,
        "Units": "psi"
    },

    "Temperature_Sensor": {
        "Reading": 81.2,
        "Valid": True,
        "Units": "°C"
    },

    "Flow_Rate_Sensor": {
        "Reading": 8.2,
        "Valid": True,
        "Units": "kg/s"
    }
}
```

This structure allows sensor information to remain organized while making it easier to expand the framework with additional measurements in the future.

---

## Example Report

A successful measurement cycle may produce output similar to:

```text
============================
EDAF REPORT
============================

Timestamp: 2026-07-17 03:03:31

Pressure Sensor           124.2 psi    PASS
Temperature Sensor        81.2  °C     PASS
Flow Rate Sensor          8.2   kg/s   PASS

Sensor Data Logged Successfully
```

If a measurement falls outside its acceptable operating range, the program identifies the measurement as invalid and prevents the measurement set from being logged.

---

## CSV Data Logging

Validated measurements are stored in a CSV file for later review and analysis.

The CSV logger:

- Creates the data file when necessary
- Adds column headers to newly created files
- Appends new measurement records
- Includes timestamps
- Stores measurement values and engineering units
- Maintains a structured record of engineering data

This provides a simple foundation for future data analysis and visualization.

---

## Input Validation

EDAF includes exception handling to prevent invalid text or incorrectly formatted numerical input from interrupting the program.

For example, if a user enters a non-numeric value where a sensor measurement is expected, the program requests another value rather than terminating unexpectedly.

This improves program reliability and demonstrates defensive programming practices.

---

## Engineering Value

EDAF demonstrates how software can be applied to instrumentation and engineering measurement workflows.

The project combines concepts from:

- Sensor measurements
- Instrumentation
- Data acquisition
- Measurement validation
- Python programming
- Data organization
- Error handling
- Engineering reporting
- CSV data storage

The modular architecture also makes the program easier to expand as additional sensors, reporting features, graphing capabilities, or data-acquisition interfaces are introduced.

EDAF represents an important step in combining my interests in software development, controls and instrumentation, and engineering data analysis.

---

## Future Development

Potential future enhancements include:

- Additional sensor types
- Automated graph generation
- Historical measurement analysis
- Expanded reporting
- Alarm and warning thresholds
- Sensor configuration files
- Real-time measurement visualization
- Integration with external data-acquisition hardware
- Automated engineering report generation

---

## Project Status

**In Development**

Current functionality includes:

- Sensor measurement input
- Numeric input validation
- Pressure validation
- Temperature validation
- Flow-rate validation
- PASS/FAIL reporting
- Timestamp generation
- Structured measurement storage
- CSV data logging
- Formatted console reports

---

## Disclaimer

EDAF is currently a **software-based engineering data-acquisition framework and simulation project**.

The current version demonstrates measurement input, validation, reporting, and data logging using software-generated or manually entered values. It does not claim direct integration with physical DAQ hardware or production instrumentation systems.
