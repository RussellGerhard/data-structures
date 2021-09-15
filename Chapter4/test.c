#include <stdio.h>

int main() {
    printf("Hello World!\n");
    int balance[5] = {10, 20, 30, 40, 50};
    printf("Size: %lu\n", sizeof(balance)/sizeof(balance[0]));
}
