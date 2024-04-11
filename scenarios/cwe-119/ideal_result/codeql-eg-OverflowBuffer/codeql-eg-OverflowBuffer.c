#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    const char* message = "Hello";
    char buffer[256];

    // 将消息复制到缓冲区，确保不会超出缓冲区的大小
    memcpy(buffer, message, strlen(message) + 1);
    // 在目标缓冲区中的剩余空间处填充零，以确保字符串终止符
    memset(buffer + strlen(message), 0, sizeof(buffer) - strlen(message) - 1);

    return 0;
}