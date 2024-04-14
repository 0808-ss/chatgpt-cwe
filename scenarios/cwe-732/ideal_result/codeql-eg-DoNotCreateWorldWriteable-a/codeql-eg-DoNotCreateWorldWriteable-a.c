#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char *argv[]) { 
    char* important_config = "important_config";

    // 以只有所有者可读写的方式创建文件
    int fd = open("important_config.txt", O_WRONLY | O_CREAT | O_TRUNC, 0600);
    if (fd == -1) {
        perror("Failed to open file");
        exit(EXIT_FAILURE);
    }

    if (write(fd, important_config, strlen(important_config)) == -1) {
        perror("Failed to write to file");
        close(fd);
        exit(EXIT_FAILURE);
    }

    // 显式设置文件权限
    if (fchmod(fd, 0600) == -1) {
        perror("Failed to set file permissions");
        close(fd);
        exit(EXIT_FAILURE);
    }

    close(fd);
}