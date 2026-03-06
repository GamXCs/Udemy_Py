# Number Parser

A small Python module for safely parsing integers and floating-point numbers from strings.

## Features

- Handles leading and trailing whitespace
- Supports optional `+` and `-` signs
- Validates numeric input
- Custom exception for parsing errors

## Installation

Clone the repository:

```bash
git clone <repo-url>
```

## Example Usage

```python
from number_parser.parser import parse_int, parse_float

print(parse_int("   -123   "))
print(parse_float("3.14"))
print(parse_float(".5"))
print(parse_float("5."))
print(parse_float("   -0.25   "))
```

## Project Structure

```
number_parser
├── README.md
├── examples
│   └── demo.py
├── src
│   └── number_parser
│       ├── __init__.py
│       └── parser.py
└── tests
```

## Future Improvements

- `parse_number()` dispatcher
- scientific notation support (`1e6`)
- more automated tests
