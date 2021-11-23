#include <stdio.h>

#define max_num 6

int main()
{
    int *a;
    int b = 10;
    a = &b;
    printf("%d",*a);
}