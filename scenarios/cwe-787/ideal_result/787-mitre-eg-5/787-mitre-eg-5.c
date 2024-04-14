#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    
    // 确保提供了一个参数
    if (argc != 2) {
        printf("需要提供一个参数\n");
        exit(1);
    }

    // 获取参数
    char *input = argv[1];
    
    // 打印参数
    printf("'%s'\n", input);

    // 修剪末尾的空白字符
    int length = strlen(input);
    while (length > 0 && (input[length - 1] == ' ' || input[length - 1] == '\t' || input[length - 1] == '\n' || input[length - 1] == '\r')) {
        input[length - 1] = '\0';
        length--;
    }

    printf("修剪后: '%s'\n", input);

    return 0;
}