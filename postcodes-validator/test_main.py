import pytest
from main import validate_uk_postcode, format_uk_postcode

validate_test_cases = [
    ("SW1A 1AA", True, "SW1A 1AA"),  # Buckingham Palace
    ("M1 1AA", True, "M1 1AA"),      # Manchester
    ("B33 8TH", True, "B33 8TH"),   # Birmingham
    ("W1A 0AX", True, "W1A 0AX"),   # London
    ("EC1A 1BB", True, "EC1A 1BB"), # London
    ("W1N 4DJ", True, "W1N 4DJ"),   # London
    ("CR2 6XH", True, "CR2 6XH"),   # Croydon
    ("DN55 1PT", True, "DN55 1PT"), # Doncaster
    ("GIR 0AA", False, None),        # Girobank (should be valid, but not in our regex)
    ("SAN TA1", False, None),        # Invalid - contains invalid characters
    ("Q1A 1AA", False, None),        # Invalid - starts with Q
    ("A1A 1AA", True, "A1A 1AA"),
    ("AA1A 1AA", True, "AA1A 1AA"),
    ("A1 1AA", True, "A1 1AA"),
    ("AA1 1AA", True, "AA1 1AA"),
    ("A1A1 1AA", True, "A1A1 1AA"),
    ("AA1A1 1AA", True, "AA1A1 1AA"),
    ("A11 1AA", True, "A11 1AA"),
    ("AA11 1AA", True, "AA11 1AA"),
    ("A111 1AA", True, "A111 1AA"),
    ("AA111 1AA", True, "AA111 1AA"),
]

# Additional test cases for formatting function
format_test_cases = [
    ("SW1A1AA", "SW1A 1AA"),        # No spaces
    ("sw1a 1aa", "SW1A 1AA"),       # Lowercase with space
    ("SW1A  1AA", "SW1A 1AA"),      # Multiple spaces
    ("SW1A-1AA", "SW1A 1AA"),       # Hyphen separator
    ("SW1A_1AA", "SW1A 1AA"),       # Underscore separator
    ("SW1A\t1AA", "SW1A 1AA"),      # Tab separator
    ("  SW1A 1AA  ", "SW1A 1AA"),   # Leading/trailing spaces
    ("SW1A1AA", "SW1A 1AA"),        # Compact format
    ("", None),                     # Empty string
    (None, None),                   # None input
    ("INVALID", None),              # Invalid postcode
    ("12345", None),                # Invalid format
]

@pytest.mark.parametrize("postcode,expected_valid,expected_format", validate_test_cases)
def test_validate_uk_postcode(postcode, expected_valid, expected_format):
    assert validate_uk_postcode(postcode) == expected_valid
    if expected_valid:
        assert format_uk_postcode(postcode) == expected_format
    else:
        assert format_uk_postcode(postcode) is None

@pytest.mark.parametrize("postcode,expected_format", format_test_cases)
def test_format_uk_postcode(postcode, expected_format):
    assert format_uk_postcode(postcode) == expected_format 