#include <stdio.h>
#include <stdlib.h>

extern int getMonthlySales(int month);

int main(int argc, char *argv[]) {
    int total_sales = 0;

    // sum the number of sales for the first quarter
    for (int month = 1; month <= 3; month++) {
        total_sales += getMonthlySales(month);
    }

    printf("Total sales for the first quarter: %d\n", total_sales);
    return 0;
}