#include <stdio.h>

int main(void) {
    int w = 0;
    scanf("%d", &w);
        if (w % 2 == 0 && w > 2) {
            printf("YES\n");
        }else {
            printf("NO\n");
        }
        return 0;
}