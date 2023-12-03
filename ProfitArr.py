"""
ArrChallenge(arr) is a function that takes the array of numbers stored in arr which will contain integers that represents the amount in dollars that a single stock
is worth, and return maximum profit that could have been made by buying stock on day d and selling stock on day y where y>x for example if arr is [44,30,24,32,35,30,40,38,15]
then your program should return 16 because at index 2 the stock was worth $24 and at index 6 stock was worth $40,cso if you bought the stock at at 24 and sold it at 40 you would have
made a profit of $16, which is the maximum peofit that could have made with list of stock prices.
if there is no profit that could have been made with stock prices, then your program should return -1.
"""
def ArrayProfit(arr):
    if len(arr) < 2:
        return -1 # cannot make a profit with less than two days of stock data
    
    buy_price = arr[0]
    max_profit = -1 # initialize with -1 to handle cases where no profit is possible

    for price in arr[1:]:
        current_profit = price - buy_price

        if current_profit > max_profit:
            max_profit = current_profit

        if price < buy_price:
            buy_price = price
    
    return max_profit

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(ArrayProfit(arr))

 #Comment

"""
A step-by-step explanation of the selected code:

1. The function `ArrayProfit` is defined, which takes a list of integers `arr` as an argument. Each integer in `arr` represents the stock price on a particular day.

2. The function first checks if the length of `arr` is less than 2. If it is, the function returns `-1` because it's impossible to make a profit with less than two days of stock data.

3. The variable `buy_price` is initialized with the first price in `arr`. This represents the price at which the stock is bought.

4. The variable `max_profit` is initialized with `-1`. This represents the maximum profit that can be made. It's initialized with `-1` to handle cases where no profit is possible.

5. The function then iterates over each price in `arr` starting from the second price. For each price, it calculates the profit that can be made if the stock is sold at that price (`current_profit = price - buy_price`).

6. If `current_profit` is greater than `max_profit`, `max_profit` is updated with `current_profit`.

7. If the current price is less than `buy_price`, `buy_price` is updated with the current price. This is because buying the stock at a lower price can potentially lead to a higher profit.

8. After all prices have been processed, the function returns `max_profit`, which is the maximum profit that can be made.

9. The `if __name__ == '__main__':` block is used to test the function. If the script is run directly (not imported as a module), then `__name__` will be `'__main__'`, and the code inside this block will be executed. The `input()` function is used to read a space-separated list of integers from the user, which is passed to the `ArrayProfit` function. The result is then printed to the console.

The time complexity of this function is O(n), where n is the number of days (i.e., the length of `arr`). This is because each day is processed once. The space complexity is O(1), as the function only uses a constant amount of space to store `buy_price` and `max_profit`.
"""       


