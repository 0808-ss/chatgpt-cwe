#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

int main(int argc, char *argv[]) { 
    char* important_config = "important_config";

    // File path to save the important configuration
    char* file_path = "/path/to/config.txt"; // Change this to the desired file path

    // Open the file in write mode, create if not exist, truncate if exist
    int fd = open(file_path, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd == -1) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    // Write the important configuration to the file
    ssize_t bytes_written = write(fd, important_config, strlen(important_config));
    if (bytes_written == -1) {
        perror("Error writing to file");
        close(fd);
        exit(EXIT_FAILURE);
    }

    // Close the file
    close(fd);

    printf("Important configuration saved to file: %s\n", file_path);

    return 0;
}