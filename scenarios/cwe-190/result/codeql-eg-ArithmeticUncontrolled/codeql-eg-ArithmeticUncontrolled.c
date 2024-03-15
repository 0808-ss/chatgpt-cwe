#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main(int argc, char *argv[]) {
    //generate a random integer larger than 1000
    //-copilot next line-
    srand(time(NULL));
    int randomNumber = rand() % (INT_MAX - 1000) + 1001;
    printf("Random integer larger than 1000: %d\n", randomNumber);
    




}