
# Factorial Module Challenges

The main objective of this repo: 

- Example of a Python program calling a C function is presented in [main.py](https://github.com/kgashok/AfraidDefiniteSpyware/blob/691b87f28081460b13c0fb17213410f3f428efd2/main.py)
- Example of a C function defined in [mathlib.c](https://github.com/kgashok/AfraidDefiniteSpyware/blob/691b87f28081460b13c0fb17213410f3f428efd2/mathlib.c)

The below challenges will get you more familiar with the layout of the land. Good luck! 

## Challenge 1: Handling Large Numbers (factorial(14))

**Problem**: 
When calculating factorial(14), you'll encounter an overflow issue since the result exceeds the maximum value that can be stored in a C int type.

```python
from _mathlib import lib 
lib.factorial(14)  # Will produce incorrect result

```

## Challenge 2: Remove Debug Print Statement

**Problem**: 
The factorial_module.c contains a debug print statement that outputs calculation progress:
```c
printf("Calculating for %d\n", n);
```

After rebuilding, the factorial calculations will run silently without the debug output.

**Note**: If you need to restore the debug output later, simply uncomment the printf line and rebuild the module.
