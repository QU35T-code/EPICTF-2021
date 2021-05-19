#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <unistd.h>

void ignore_me_init_buffering()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    //setvbuf(stderr, NULL, _IONBF, 0);
}

void kill_on_timeout(int sig)
{
    if (sig == SIGALRM) {
        printf("[!] Anti DoS Signal");
        exit(0);
    }
}

void ignore_me_init_signal()
{
    signal(SIGALRM, kill_on_timeout);
    alarm(120);
}

int main(void)
{
    ignore_me_init_buffering();
    ignore_me_init_signal();
    char name[16];
    int is_admin = 0;

    printf("What is your name ?\n> ");
    scanf("%s", name);
    printf("Hello %s\n", name);
    if (is_admin != 0)
        system("/bin/bash");
    else
        printf("Sorry, you are not admin (is_admin = %x)\n", is_admin);
    return 0;
}
