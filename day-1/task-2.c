#include <stdio.h>

#define MAX_RANGE_LENGHT 1000000

int main(void)
{
    FILE *fp = NULL;
    fp = freopen("input", "r", stdin);

    int values[MAX_RANGE_LENGHT] = {0};
    int inputs[MAX_RANGE_LENGHT] = {0};
    int count = 0;
    int sum = 0;
    int val;

    values[MAX_RANGE_LENGHT / 2] = 1; // the middle val is '0', need negative 
                                      // val
    while(!feof(fp))
    {
        scanf("%d", &val);
        inputs[count] = val;
        count++;
    }

    while(1)
        for(int i = 0; i < count; i++)
        {
            sum += inputs[i];
            if(values[sum + MAX_RANGE_LENGHT / 2] == 1)
            {
                printf("%d\n", sum);
                return 0;
            }

            values[sum + MAX_RANGE_LENGHT / 2] = 1;
        }

    return 0;
}