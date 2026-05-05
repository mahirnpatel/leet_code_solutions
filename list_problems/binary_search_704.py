from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target <  nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
    def binarySearch(self, nums: [int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1 
        
        mid = (low + high) // 2
        
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.binarySearch(nums, mid+1 , high , target)
        
        return self.binarySearch(nums , low , mid- 1, target)
    
    
            
        
            

def main():
    sol = Solution()
    print(sol.search([50,40,30,20,10], 30))
    print(sol.binarySearch([50,40,30,20,10], 0, 4, 30))

if __name__ == "__main__":
    main()