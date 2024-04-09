#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    // malloc a large buffer and copy in 100 characters from stdin
    char* buf = malloc(1024);
    if (buf == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    fgets(buf, 101, stdin); // 100 characters + null terminator

    // Now you have 100 characters copied into buf
    // Use buf as needed

    // Don't forget to free the memory when done
    free(buf);
    return 0;
}