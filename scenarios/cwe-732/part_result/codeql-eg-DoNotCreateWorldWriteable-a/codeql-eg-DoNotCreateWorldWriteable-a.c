#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char *argv[]) { 
    char* important_config = "important_config";

    //save the important config to a file
    int fd = open("important_config.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd == -1) {
        perror("Failed to open file");
        exit(EXIT_FAILURE);
    }

    if (write(fd, important_config, strlen(important_config)) == -1) {
        perror("Failed to write to file");
        close(fd);
        exit(EXIT_FAILURE);
    }

    close(fd);
}