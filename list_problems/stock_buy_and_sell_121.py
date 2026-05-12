from typing import List
class Solution:
    def maxProfit_better_appraoch(self, prices: List[int]) -> int:
        #Find minimum price 
        n = len(prices)
        min_price_index = prices.index(min(prices))

        # If the min price is in last index, return 0
        if min_price_index == n - 1:
            return 0
        
        max_difference = float('-inf')
        for j in range(min_price_index+1 , n):
            if prices[j] - prices[min_price_index] > max_difference:
                max_difference = prices[j] - prices[min_price_index]
        
        return max_difference
    
    def maxProfit_optimal_approach(self, prices:List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit , price - min_price)
        return max_profit
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit_better_appraoch([7,1,5,3,6,4]))
    print(sol.maxProfit_better_appraoch([7,6,4,3,1]))
    print(sol.maxProfit_optimal_approach([2,4,1]))