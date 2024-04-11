#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[]) {
    // 检查参数数量
    if (argc != 2) {
        printf("Usage: %s <username>\n", argv[0]);
        return 1;
    }

    // 构造命令参数数组
    char *args[] = { "getent", "passwd", argv[1], NULL };

    // 执行命令
    execvp(args[0], args);

    // 如果execvp执行失败，输出错误信息并退出程序
    perror("execvp");
    return 1;
}