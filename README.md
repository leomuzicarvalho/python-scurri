# Python Scurri

Simple three-five sequence generator with type hints.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```python
from scurri import three_five_sequence, print_three_five

# Get sequence as list
result = three_five_sequence(1, 15)

# Print sequence
print_three_five(1, 20)
```

## Test

```bash
pytest test_scurri.py
```

## Type Check

```bash
mypy scurri.py test_scurri.py
```
