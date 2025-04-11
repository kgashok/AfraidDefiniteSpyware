from cffi import FFI

ffi = FFI()

# Define the C function interface
ffi.cdef("""
    unsigned int fact(int a);
""")


# Compile the C code
ffi.set_source("_mathlib",
    """ 
    unsigned int fact(unsigned int a);
    """,
    sources=["mathlib.c"])

if __name__ == '__main__':
    ffi.compile()
    from _mathlib import lib

    inp = input("Enter a number: ")
    inp = int(inp)
    result = lib.fact(inp)
    print(f"Result from C function: {result:_}")

    result2 = lib.fact(inp+1)
    print(f"Result from C function: {result2:_}")

    assert (result2 > result)