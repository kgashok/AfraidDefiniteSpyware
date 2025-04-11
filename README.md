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

The module uses unsigned int for calculations, which means:
- Maximum supported input is 13 (13! =  1_932_053_504)
- Numbers larger than 13 will raise an OverflowError


## Running the Program

Click the "Run" button in Replit, or run:

```bash
python3 main.py
```

When prompted, enter a number between 0 and 13 to calculate its factorial.
