from cffi import FFI

ffi = FFI()

# Define the C function interface
ffi.cdef("""
    int factorial(int a);
""")


# Compile the C code
ffi.set_source("_mathlib",
    """ 
    int factorial(int a);
    """,
    sources=["mathlib.c"])

if __name__ == '__main__':
    ffi.compile()

    
    from _mathlib import lib
    
    inp = input("Enter a number: ")
    inp = int(inp)
    result = lib.factorial(inp)
    
    print(f"Result from C function for {inp}: {result:_}")

    result2 = lib.factorial(inp+1)
    print(f"Result from C function for {inp+1}: {result2:_}")

    assert (result2 > result)

