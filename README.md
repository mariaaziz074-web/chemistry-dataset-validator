# Chemistry Dataset Validator

A lightweight Python tool for detecting common quality problems in chemistry datasets.

## Problem

Experimental chemistry datasets can contain missing values, duplicate rows, incorrect data types, missing required columns, or physically invalid negative values.

This project provides a simple automated validation workflow for a CSV dataset.

## Approach

The validator uses Pandas to:

- Check required columns
- Report dataset dimensions
- Detect missing values
- Detect duplicate rows
- Inspect numerical data types
- Detect negative values in numerical chemistry variables
- Return PASSED or FAILED validation status

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv-1