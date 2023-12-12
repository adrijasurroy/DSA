# Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Examples
# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and 
# sell on day 5 (price = 6), profit = 6-1 = 5.

# Note: That buying on day 2 and selling on day 1 
# is not allowed because you must buy before 
# you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are 
# done and the max profit = 0.
import sys
def maxprofit(arr)->int:
    # maxp= -sys.maxsize -1
    maxp=0
    minprice = float("inf")
    # mindiff = arr[0]
    n = len(arr)
    for i in range(1,n):
        minprice = min(minprice, arr[i])
        maxp = max(maxp,arr[i]-minprice)
        
    return maxp
    
if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    maxPro = maxprofit(arr)
    print("Max profit is:", maxPro)