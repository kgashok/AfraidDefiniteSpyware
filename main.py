
from cffi import FFI

ffi = FFI()

# Define the C function interface
ffi.cdef("""
    int add(int a, int b);
""")

# Create a C source file
with open("mathlib.c", "w") as f:
    f.write("""
        int add(int a, int b) {
            return a + b;
        }
    """)

# Compile the C code
ffi.set_source("_mathlib",
    """ 
    int add(int a, int b);
    """,
    sources=["mathlib.c"])

if __name__ == '__main__':
    ffi.compile()
    from _mathlib import lib
    result = lib.add(5, 3)
    print(f"Result from C function: {result}")
