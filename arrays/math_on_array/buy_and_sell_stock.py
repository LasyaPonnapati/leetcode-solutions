# LeetCode 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock
# on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

# Approach 1 (check every pair):
# 1. Try every pair of days: buy on day i, sell on a later day j.
# 2. Profit for that pair is prices[j] - prices[i].
# 3. Keep the largest profit seen. If every pair loses money, profit stays 0.

# Time Complexity: O(n^2) - the outer loop runs n times, and for each buy day
# the inner loop checks every later sell day.
# Space Complexity: O(1) - only the length and the best profit are stored.

class Solution:
    def maxProfit(self, arr: list[int]) -> int:
        n=len(arr)
        profit=0
        for i in range(0,n):
            for j in range(i+1,n):
                if arr[j]-arr[i]>profit:
                    profit = arr[j]-arr[i]
        return profit

# Approach 2 (track the cheapest buy so far):
# 1. Walk the prices once from left to right.
# 2. Keep the smallest price seen so far. That is the best day to buy before today.
# 3. If today's price is lower, update that cheapest price.
# 4. Otherwise, profit if you sell today is today's price minus the cheapest price.
#    Keep the largest of those profits.
# 5. Selling is always after buying, because the cheapest price comes from an earlier day.

# Time Complexity: O(n) - each price is visited once.
# Space Complexity: O(1) - only the cheapest price and the best profit are stored.

class Solution:
    def maxProfit(self, arr: list[int]) -> int:
        min_price=arr[0]
        profit=0
        for i in arr:
            if i<min_price:
                min_price=i
            elif i-min_price>profit:
                profit=i-min_price
        return profit
