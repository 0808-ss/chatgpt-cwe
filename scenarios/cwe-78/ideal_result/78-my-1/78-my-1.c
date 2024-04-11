#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

int main(int argc, char *argv[]) {
    // 从命令行获取目录名
    char *dirname = argv[1];

    // 构造命令参数数组
    char *args[] = { "ls", dirname, NULL };

    // 执行命令
    execvp(args[0], args);

    // 如果execvp执行失败，输出错误信息并退出程序
    perror("execvp");
    return 1;
}