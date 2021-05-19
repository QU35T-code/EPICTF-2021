#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char buff[256];

    printf("What do you want to store in my buffer?\n> ");
    fgets(buff, 256, stdin);
    ((void (*)()) buff)();
    return 0;
}