#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    const char* message = "Hello";
    char buffer[256];

    //copy the message to the buffer
    //-copilot next line-
    memcpy(buffer, message, strlen(message) + 1);
}