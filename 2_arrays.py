# Example: Say you are storing Apple's stock prices for 5 days 
stock_prices=[297, 330, 559, 785, 906]
# Scenario 1: Looking for the stock price on day 3:
day_2_stock_price=stock_prices[2]
print(day_2_stock_price)
# The big O complexity of looking for an array element by index is O(1) meaning, it's a constant time operation.

# SCENARIO 2: ON WHAT DAY WAS PRICE 785?
# Here you're not looking by index, but by value
stock_prices=[297, 330, 559, 785, 906]
def get_stock_price(stock_price):
    stock_price_index=len(stock_prices)
    for i in range(stock_price_index):
        if stock_prices[i]==785:
            return i
        
answer=get_stock_price(785)
print(answer)