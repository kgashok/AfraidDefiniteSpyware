
#include <stdio.h> 

unsigned int
fact(unsigned int n) {
    printf("Calculating for %d\n", n);
    if (n <= 1) return 1;
    return n * fact(n - 1);
}

