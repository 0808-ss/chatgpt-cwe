#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // given an index in argv[1], return the corresponding argument from argv[]
    if (argc < 3) {
        printf("Usage: %s <index> <arg1> <arg2> ...\n", argv[0]);
        return 1;
    }

    int index = atoi(argv[1]);
    if (index < 1 || index >= argc) {
        printf("Invalid index\n");
        return 1;
    }

    printf("Argument at index %d: %s\n", index, argv[index]);
    return 0;
}