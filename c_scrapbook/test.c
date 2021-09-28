#include <stdio.h>

int main() {
    printf("Hello World!\n");
    int balance[5];
    balance[0] = 10;
    balance[4] = 40;
    printf("%u\n", balance[0]);
    printf("%u\n", balance[1]);
    printf("%u\n", balance[2]);
    printf("%u\n", balance[3]);
    printf("%u\n", balance[4]);
    printf("Size: %lu\n", sizeof(balance)/sizeof(balance[1]));
}
