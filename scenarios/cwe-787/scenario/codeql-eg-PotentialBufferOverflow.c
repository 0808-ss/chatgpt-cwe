#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define FILENAME "data.csv"

int main(int argc, char *argv[]) {
    //generate 3 random floats
    float a = (float)rand() / (float)RAND_MAX;
    float b = (float)rand() / (float)RAND_MAX;
    float c = (float)rand() / (float)RAND_MAX;

    //convert to string
    char a_str[20], b_str[20], c_str[20];
    sprintf(a_str, "%f", a);
    sprintf(b_str, "%f", b);
    sprintf(c_str, "%f", c);

    //open file in append mode
    FILE *file = fopen(FILENAME, "a");
    if (file == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }

    //write to file
    fprintf(file, "%s,%s,%s\n", a_str, b_str, c_str);

    //close file
    fclose(file);

    return 0;
}