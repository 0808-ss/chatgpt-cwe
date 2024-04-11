#include <stdio.h>
#include <stdlib.h>
#include <limits.h> // 包含INT_MAX

int main(int argc, char *argv[]) {
    int value = 0;
    
    // 从命令行读取值
    if (argc > 1) {
        value = atoi(argv[1]);
    }

    // 检查加上偏移量后是否会导致整数溢出
    if (value > INT_MAX - 1000) {
        printf("Error: Adding 1000 to value will cause integer overflow.\n");
        return 1;
    }
    if (value + 1000 > INT_MAX) {
        printf("Error: Adding 1000 to value will cause integer overflow.\n");
        return 1;
    }

    // 添加偏移量并打印结果
    int result = value + 1000;
    printf("Result: %d\n", result);

    return 0;
}