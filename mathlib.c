
#include <stdio.h> 

int
factorial(int n) {
    printf("Calculating for %d\n", n);
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

