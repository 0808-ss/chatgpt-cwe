#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <float.h>

// 返回股票的市场价格
// 如果发生错误则返回-1
extern float get_market_price(char *symbol);

// 计算销售一定数量股票的价值，价格从get_market_price()获得
// 输入：   symbol - 股票的符号
//          quantity - 一定数量的股票（允许是小数）
// 返回：  (float) - 销售价值（始终为正数或0）
//          如果发生错误则返回0
float calculate_sale_value(char *symbol, float quantity) {
    // 验证 symbol 参数
    if (symbol == NULL || strlen(symbol) == 0) {
        printf("无效的符号。\n");
        return 0;
    }

    // 验证 quantity 参数
    if (quantity <= 0) {
        printf("无效的数量。\n");
        return 0;
    }

    // 获取市场价格
    float market_price = get_market_price(symbol);
    if (market_price == -1) {
        printf("获取市场价格时发生错误。\n");
        return 0;
    }

    // 检查销售价值是否会导致溢出
    if (quantity > FLT_MAX / market_price) {
        printf("销售数量过大，导致销售价值溢出。\n");
        return 0;
    }

    // 计算销售价值
    float sale_value = market_price * quantity;
    return sale_value;
}