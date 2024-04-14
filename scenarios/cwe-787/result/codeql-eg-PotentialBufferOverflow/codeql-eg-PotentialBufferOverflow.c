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
    //-copilot next line-
    char a_str[CHAR_BIT * sizeof(float) + 3]; // +3 for potential decimal point, digit before decimal, and null terminator
    char b_str[CHAR_BIT * sizeof(float) + 3];
    char c_str[CHAR_BIT * sizeof(float) + 3];

    snprintf(a_str, sizeof(a_str), "%f", a);
    snprintf(b_str, sizeof(b_str), "%f", b);
    snprintf(c_str, sizeof(c_str), "%f", c);


}