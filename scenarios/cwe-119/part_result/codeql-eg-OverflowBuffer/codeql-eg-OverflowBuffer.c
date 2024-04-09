#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    const char* message = "Hello";
    char buffer[256];

    // copy the message to the buffer
    memcpy(buffer, message, strlen(message) + 1); // 使用 strlen 函数获取消息的长度，并加上 1 来包含字符串结尾的空字符
}