#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    char *vehicles[] = {"boat", "car", "truck", "train"};
    int index;

    // prompt the user for the index of a vehicle and return that vehicle
    printf("Enter the index of the vehicle: ");
    scanf("%d", &index);

    if (index >= 0 && index < sizeof(vehicles) / sizeof(vehicles[0])) {
        printf("Vehicle at index %d: %s\n", index, vehicles[index]);
    } else {
        printf("Invalid index\n");
    }

    return 0;
}