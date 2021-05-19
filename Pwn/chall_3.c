#include <stdio.h>
#include <stdlib.h>

void shell(void)
{
    system("/bin/bash");
}

void not_admin(void)
{
    printf("Sorry, you are not admin...\n");
}

int main(void)
{
    char name[16];
    void (*func)() = &not_admin;

    printf("shell: %p\n", shell);
    printf("What is your name ?\n> ");
    scanf("%s", name);
    printf("Hello %s\n", name);
    (*func)();
    return 0;
}