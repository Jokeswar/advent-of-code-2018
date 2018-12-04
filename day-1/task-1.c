#include <stdio.h>

int main(void)
{
    int val;
    int sum = 0;

    while(scanf("%d", &val))
        sum += val;

    printf("%d\n", sum);

    return 0;
}