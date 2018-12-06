#include <stdio.h>
#include <string.h>

#define LEN 100000

int main(void)
{
    const int dist = 'a' - 'A';
    FILE *fp = NULL;
    fp = freopen("input", "r", stdin);

    char string[LEN] = {0};
    fgets(string, LEN, fp);

    int mod = 1;

    while(mod == 1)
    {
        mod = 0;
        int len = strlen(string);
        for(int i = 0; i < len; i++)
            if(string[i] + dist == string[i + 1] || 
               string[i] == string[i + 1] + dist)
            {
                memmove(string + i, string + i + 2, len - i - 1);
                mod = 1;
            }
    }

    printf("%ld\n", strlen(string));

    return 0;
}