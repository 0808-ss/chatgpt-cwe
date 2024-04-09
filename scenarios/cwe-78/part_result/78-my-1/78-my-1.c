#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    // 从命令行参数获取目录名
    char *dirname = argv[1];

    // 构建用于执行命令的字符串
    char cmd[256] = {0};
    snprintf(cmd, sizeof(cmd), "ls %s", dirname);

    // 使用系统调用执行命令
    system(cmd);
    
    return 0;
}