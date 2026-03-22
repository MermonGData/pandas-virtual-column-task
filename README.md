# Pandas Virtual Column Utility

A robust Python utility designed to safely perform arithmetic operations on DataFrame columns based on string-based "roles." This tool uses regular expressions for strict validation and integrates into pandas-based data pipelines.

## Features
- **Regex Validation**: Ensures roles only contain allowed characters (`a-z`, `A-Z`, `_`, `+`, `*`, `-`).
- **Dynamic Summation**: Automatically parses string roles to identify and sum target columns.
- **Error Handling**: Gracefully manages empty DataFrames and missing columns.

## Tech Stack
- **Language**: Python 3.10+
- **Library**: [pandas](https://pandas.pydata.org/)
- **Testing**: [pytest](https://docs.pytest.org/)

## Getting Started

### Installation
Ensure you have the dependencies installed via the `pyproject.toml`:
```bash
pip install .
```
