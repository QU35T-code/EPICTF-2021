#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char name[16];
    int is_admin = 0;

    printf("What is your name ?\n> ");
    scanf("%s", name);
    printf("Hello %s\n", name);
    printf("is_admin = %x\n", is_admin);
    if (is_admin == 0xdeadbeaf)
        system("/bin/bash");
    else
        printf("Sorry, you are not admin (is_admin = %x)\n", is_admin);
    return 0;
}