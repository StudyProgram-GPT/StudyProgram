#include <stdio.h>
int main(int argc, char const *argv[])
{
    int a, b, c, d, e;
    int sum;
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e); 
    sum = c * d + a - b;
    printf("%d\n", sum);
    return 0;
}