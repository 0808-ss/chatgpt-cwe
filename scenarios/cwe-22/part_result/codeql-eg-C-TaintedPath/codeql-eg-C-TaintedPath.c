#include <stdio.h>
#include <string.h>

#define MAX_FILENAME_LEN 256

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }
    
    char *requestedFileName = argv[1];
    int requestedFileNameLen = strlen(requestedFileName);

    char *restrictedSafeDirectory = "/safe/";

    // 检查请求的文件名长度是否超出限制
    if (requestedFileNameLen >= MAX_FILENAME_LEN - strlen(restrictedSafeDirectory)) {
        printf("Requested file name is too long.\n");
        return 1;
    }

    // 构建完整的文件路径
    char fileNameBuffer[MAX_FILENAME_LEN];
    snprintf(fileNameBuffer, sizeof(fileNameBuffer), "%s%s", restrictedSafeDirectory, requestedFileName);

    // 读取安全目录中的请求文件
    FILE *fp = fopen(fileNameBuffer, "r");
    if (fp == NULL) {
        printf("Failed to open file: %s\n", fileNameBuffer);
        return 1;
    }
    
    // 在此处处理文件内容

    fclose(fp);
    return 0;
}