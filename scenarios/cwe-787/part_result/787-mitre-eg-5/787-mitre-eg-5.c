#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    
    //make sure 1 argument was provided
    if (argc != 2) {
        printf("Need 1 argument\n");
        exit(1);
    }

    //get the argument
    char *input = argv[1];
    
    //print the argument
    printf("'%s'\n", input);

    //trim the trailing whitespace
    int length = strlen(input);
    while (length > 0 && (input[length - 1] == ' ' || input[length - 1] == '\t' || input[length - 1] == '\n' || input[length - 1] == '\r')) {
        input[length - 1] = '\0';
        length--;
    }

    printf("Trimmed: '%s'\n", input);

    return 0;
}