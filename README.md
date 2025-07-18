# Python Scurri

A Python project containing two main utilities:

1. Three-Five sequence generator with type hints
2. UK postcode validator and formatter

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Three-Five Sequence Generator

Generates sequences where multiples of 3 are replaced with "Three", multiples of 5 with "Five", and multiples of both with "ThreeFive".

### Usage

```python
from three_five.main import three_five_sequence

# Get sequence as list
result = three_five_sequence(1, 15)
# Returns: [1, 2, 'Three', 4, 'Five', 'Three', 7, 8, 'Three', 'Five', 11, 'Three', 13, 14, 'ThreeFive']
```

## UK Postcode Validator

Validates and formats UK postcodes according to official standards.

### Usage

```python
from postcodes_validator.main import validate_uk_postcode, format_uk_postcode

# Validate a postcode
is_valid = validate_uk_postcode("SW1A 1AA")  # Returns: True
is_valid = validate_uk_postcode("INVALID")   # Returns: False

# Format a postcode
formatted = format_uk_postcode("SW1A1AA")    # Returns: "SW1A 1AA"
formatted = format_uk_postcode("sw1a 1aa")   # Returns: "SW1A 1AA"
formatted = format_uk_postcode("INVALID")    # Returns: None
```

### Features

- Validates UK postcode format (A[A]N[A/N] NAA)
- Handles various input formats (with/without spaces, hyphens, case)
- Applies official UK postcode validation rules
- Formats postcodes to standard format with proper spacing

## Testing

### Run All Tests (Recommended)

```bash
python run_tests.py
```

### Run Tests Individually

Run tests from each individual directory:

```bash
# Test three-five sequence generator
cd three-five
pytest

# Test postcode validator
cd ../postcodes-validator
pytest
```
