#include <stdio.h>
int main(int argc, char const *argv[])
{
    int a, b, c, d=57;
    int sum;
    scanf("%d %d %d", &a, &b, &c); 
    sum = c * d + a - b;
    printf("%d\n", sum);
    return 0;
}