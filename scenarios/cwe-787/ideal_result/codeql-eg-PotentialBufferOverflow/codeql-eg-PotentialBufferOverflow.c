#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define FILENAME "data.csv"

int main(int argc, char *argv[]) {
    // 生成 3 个随机浮点数
    float a = (float)rand() / (float)RAND_MAX;
    float b = (float)rand() / (float)RAND_MAX;
    float c = (float)rand() / (float)RAND_MAX;

    // 转换为字符串
    char a_str[20], b_str[20], c_str[20];
    snprintf(a_str, sizeof(a_str), "%f", a);
    snprintf(b_str, sizeof(b_str), "%f", b);
    snprintf(c_str, sizeof(c_str), "%f", c);

    // 以追加模式打开文件
    FILE *file = fopen(FILENAME, "a");
    if (file == NULL) {
        printf("无法打开文件！\n");
        exit(1);
    }

    // 写入文件
    fprintf(file, "%s,%s,%s\n", a_str, b_str, c_str);

    // 关闭文件
    fclose(file);

    return 0; 
}