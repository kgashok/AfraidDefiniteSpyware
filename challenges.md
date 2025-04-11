
# Factorial Module Challenges

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
