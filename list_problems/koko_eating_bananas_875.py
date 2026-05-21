from typing import List
import math
class Solution:
    def calculateTotalHours(self, piles , speed):
        totalH = 0
        for bananas in piles:
            totalH += math.ceil(bananas / speed)
        
        return totalH
            
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        
        low , high = 1 , maxPile
        ans = maxPile
        
        
        while low <= high:
            mid = (low + high) // 2
            totalHours = self.calculateTotalHours(piles , mid)
            
            if totalHours <= h:
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1
                
        return ans

def main():
    sol = Solution()
    print(sol.minEatingSpeed([3,6,7,11] , 8))
    print(sol.minEatingSpeed([30,11,23,4,20] , 5))
    
if __name__ == "__main__":
    main()