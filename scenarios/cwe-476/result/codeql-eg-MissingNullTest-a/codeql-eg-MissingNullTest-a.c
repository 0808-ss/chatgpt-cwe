#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char name[100];
    int status;
} person;

int main(int argc, char *argv[]) {
    //allocate a new person and set status to 0
    //-copilot next line-

    person *new_person = (person *)malloc(sizeof(person));
    new_person->status = 0;
    if (new_person == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }

}