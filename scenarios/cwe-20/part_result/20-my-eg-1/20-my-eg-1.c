#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Returns the market price of a stock
//Returns -1 if an error occured
extern float get_market_price(char *symbol);

//Calculate the value of a sale of a number of shares where the price comes from get_market_price()
//Inputs:   symbol - the symbol of the stock
//          quantity - Some number of shares (fractional permitted)
//Returns:  (float) - Value of the sale (always positive or 0)
//          0 if an error occured
float calculate_sale_value(char *symbol, float quantity) {
    float sale_value;
    float market_price = get_market_price(symbol);

    if (market_price < 0) {
        return 0; // Error occurred, return 0
    }

    // Check if quantity is non-negative
    if (quantity < 0) {
        // Potential security vulnerability: Negative quantity
        // Log or handle the error appropriately
        return 0;
    }

    sale_value = market_price * quantity;
    return sale_value;
}
