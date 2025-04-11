# Python-C Factorial Module Example

This project demonstrates how Python integrates with a C language function to calculate factorials.

# C Factorial function

This is currently edited and modified in ```mathlib.c```. Change the code as you deem fit. 

## Usage Example

```python

from _mathlib import lib
result = lib.factorial(5)

```

## Limitations

The module uses int for calculations, which means:
- Maximum supported input is 12 (12! =  479_001_600)
- Numbers larger than 12 will raise an OverflowError
    - For 13! it should be = 6_227_020_800



## Running the Program

Click the "Run" button in Replit, or run:

```bash
python3 main.py
```

When prompted, enter a number between 0 and 13 to calculate its factorial.
