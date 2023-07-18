#include <stdio.h>
int main(int argc, char const *argv[])
{
    int a, b, c, d;
    int sum;
    scanf("%d %d %d %d", &a, &b, &c, &d); 
    sum = a + b - (c * d);
    printf("%d\n", sum);
    return 0;
}