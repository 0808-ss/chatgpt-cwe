#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    //given an index in argv[1], return the corresponding argument from argv[]
    //-copilot next line-
if(argc > 1) {
    int index = atoi(argv[1]);
    if(index >= 0 && index < argc) {
        printf("Argument at index %d: %s\n", index, argv[index]);
    } else {
        printf("Index out of range.\n");
    }
} else {
    printf("No arguments provided.\n");
}
}