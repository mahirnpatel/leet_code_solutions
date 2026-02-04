from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            
            if len(window) > k:
                window.remove(nums[i-k])
        return False
    
def main():
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,23,4] , 3))
    print(sol.containsNearbyDuplicate([1,2,3,1] , 3))
    print(sol.containsNearbyDuplicate([1,2,3,1,2,3] , 2))

if __name__ =='__main__':
    main()