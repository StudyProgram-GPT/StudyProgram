#include <stdio.h>
int main(int argc, char const *argv[])
{
    int a, b, c, d;
    int sum;
    scanf("入力:%d %d %d %d", &a, &b, &c, &d); 
    sum = c * d + a - b;
    printf("%d\n", sum);
    return 0;
}