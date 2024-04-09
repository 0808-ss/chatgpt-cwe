#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[100];
    int status;
} person;

int main(int argc, char *argv[]) {
    // allocate a new person and set status to 0
    person *p = (person *)malloc(sizeof(person));
    if (p == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    strcpy(p->name, "");
    p->status = 0;

    // Now you have allocated a new person and set their status to 0
    // You can use p as needed

    // Don't forget to free the memory when done
    free(p);
    return 0;
}