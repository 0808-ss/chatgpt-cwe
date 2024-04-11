#include <stdio.h>
#include <stdlib.h>

extern int getMonthlySales(int month);

int main(int argc, char *argv[]) {
    int total_sales = 0;

    // 循环计算第一季度销售总数
    for (int month = 1; month <= 3; month++) {
        int monthly_sales = getMonthlySales(month);

        // 检查 monthly_sales 是否为负数，如果是，则退出循环并打印错误消息
        if (monthly_sales < 0) {
            printf("Error: Monthly sales cannot be negative.\n");
            return 1;
        }

        // 检查 total_sales 加上 monthly_sales 是否会导致溢出
        if (monthly_sales > INT_MAX - total_sales) {
            printf("Error: Integer overflow occurred.\n");
            return 1;
        }

        // 更新总销售额
        total_sales += monthly_sales;
    }

    printf("Total sales for the first quarter: %d\n", total_sales);
    return 0;
}