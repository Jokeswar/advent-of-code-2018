#include <stdio.h>
#include <string.h>

#define LEN 100000

void replace(char string[LEN], char chr);

int main(void)
{
    const int dist = 'a' - 'A';
    FILE *fp = NULL;
    fp = freopen("input", "r", stdin);

    char string[LEN] = {0};
    char string_copy[LEN] = {0};
    fgets(string, LEN, fp);
    strcpy(string_copy, string);
    int min = 9999999;

    for(int j = 'A'; j < 'Z'; j++)
    {
        int mod = 1;

        replace(string, j);
        replace(string, j + dist);

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
        if(strlen(string) < min)
            min = strlen(string);

        strcpy(string, string_copy);
    }

    printf("%d\n", min);

    return 0;
}

void replace(char string[LEN], char chr)
{
    int i = 0;
    int len = strlen(string);

    while(string[i] != '\0')
    {
        if(string[i] == chr)
        {
            memmove(string + i, string + i + 1, len - i);
            i--;
            len--;
        }

        i++;
    }
}