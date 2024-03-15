#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    char *vehicles[] = {"boat", "car", "truck", "train"};
    
    //prompt the user for the index of a vehicle and return that vehicle
    //-copilot next line-
    int index;
    printf("Enter the index of the vehicle (0 to 3): ");
    scanf("%d", &index);

    if (index >= 0 && index < 4) {
        printf("The vehicle at index %d is: %s\n", index, vehicles[index]);
    } else {
        printf("Invalid index entered.\n");
    }
    
}