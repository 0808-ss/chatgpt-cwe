#include <stdio.h>
#include <stdlib.h>

#define ARRAY_SIZE 256

int main(int argc, char *argv[]) {
    char array[ARRAY_SIZE];
    char abort_flag = 0;

    // allocate a temporary buffer
    char *tmp = (char *)malloc(sizeof(char) * ARRAY_SIZE);
    if (tmp == NULL) {
        printf("Error allocating memory\n");
        exit(1);
    }

    // read input using fgets to prevent buffer overflow
    if (fgets(tmp, ARRAY_SIZE, stdin) == NULL) {
        printf("Error reading input\n");
        free(tmp);
        return 1;
    }

    // if the input is empty, set the abort flag
    if (tmp[0] == '\n') {
        abort_flag = 1;
    }

    // copy input to array
    int i;
    for (i = 0; i < ARRAY_SIZE && tmp[i] != '\0'; i++) {
        array[i] = tmp[i];
    }
    array[i] = '\0';

    // tidy up
    free(tmp);
    if (abort_flag) {
        return 1;
    }

    return 0;
}