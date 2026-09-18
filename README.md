# Chemistry Dataset Validator

A Python-based validation tool for checking the quality and consistency of chemistry datasets before analysis or machine-learning workflows.

## Features

- Checks required columns
- Detects missing values
- Detects duplicate rows
- Detects non-finite numeric values (`inf` and `-inf`)
- Detects variable-specific physically invalid values
- Provides clear validation errors
- Includes automated tests with pytest

## Current Validation Rules

The validator currently checks:

- `Material`
- `Dye`
- `Bandgap_eV`
- `Concentration_mg_L`
- `Time_min`
- `Rate_constant`

It flags non-finite numeric values and values that violate defined variable-specific physical constraints.

## Installation

Clone the repository:

```bash
git clone https://github.com/mariaaziz074-web/chemistry-dataset-validator.git
cd chemistry-dataset-validator
