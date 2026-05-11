from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        
        while low <= high:
            
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            #Check if the left hald is sorted
            if nums[low] <= nums[mid]:
                # if target is in the sorted left half , search left side
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                    
                else:
                    low = mid + 1 # search on the right side
            
            else:
                #target lies in the sorted right half, search right
                
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1 
    
def main():
    sol = Solution()
    print(sol.search([4,5,6,7,8,1,2], 0))
    print(sol.search([4,5,6,7,0,1,2], 0))
    print(sol.search([4,5,6,7,0,1,2], 4))
    

if __name__ == "__main__":
    main()
    
                
                    
            
        