#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char name[100];
    int status;
} person;

int main(int argc, char *argv[]) {
    //allocate a new person
    person *p = (person *)malloc(sizeof(person));
    //set status to 0
    //-copilot next line-
    if (p == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1; // indicate failure
    }

    // set status to 0
    p->status = 0;

    // You can also set the name if needed
    // strcpy(p->name, "John Doe");

    // Your code continues here

    // Don't forget to free allocated memory when done
    free(p);


}