from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low , high = 0 , len(nums)-1
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        return low

def main():
    sol = Solution()
    print(sol.findMin([3,4,5,1,2]))                
    print(sol.findMin([4,5,6,7,0,1,2,3]))                
    print(sol.findMin([11,13,15,17]))      
    
if __name__ == "__main__":
    main()          
                