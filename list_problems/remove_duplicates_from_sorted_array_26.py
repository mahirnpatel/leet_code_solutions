# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
from typing import List
# from collections import Counter 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_element_placeholder = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[unique_element_placeholder] = nums[i]
                unique_element_placeholder += 1
        
        return unique_element_placeholder


def main():
    sol = Solution()
    print(sol.removeDuplicates([1,1,2]))  
    print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

    
if __name__ == "__main__":
    main()
    