#include <stdio.h>
int main(int argc, char const *argv[])
{
    int a, b, c, d;
    int sum;
    scanf("%d %d %d %d", &a, &b, &c, &d); 
    sum = c * d + a - b;
    printf("答えは、%d\n", sum);
    return 0;
}