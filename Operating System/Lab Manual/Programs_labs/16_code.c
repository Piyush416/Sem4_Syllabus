// #include <unistd.h>
#include <stdlib.h>

int main()
{
    pid_t p = fork();
    if (p < 0){
        perror("fork failed");
        exit(1);
    }
    else if (p == 0)
    {
        printf("Hello from Child! Process ID (PID): %d\n", getpid());
    }
    else
    {
        printf("Hello from Parent! Process ID (PID): %d\n", getpid());
    }
    return 0
}