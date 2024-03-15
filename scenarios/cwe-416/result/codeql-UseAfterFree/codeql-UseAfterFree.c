#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    //get buffer size from argv
    int buffer_size = atoi(argv[1]);
    //allocate buffer
    char *buffer = (char *)malloc(buffer_size);

    //-copilot next line-
    printf("Please enter a message: ");
    fgets(buffer, buffer_size, stdin);

    //print out the input
    printf("You entered: %s\n", buffer);

    //free the allocated memory

}