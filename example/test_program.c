#include <stdio.h>

int buggy_function(int x) {
    int *p = NULL;
    if (x > 0) {
        *p = x;  // Null pointer dereference
    }
    return x * 2;
}

int main() {
    int result = buggy_function(10);
    printf("Result is: %d\n", result);
    return 0;
}
