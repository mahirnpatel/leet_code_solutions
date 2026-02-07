from typing import List
class Solution:
    def majority_element_brute_approach(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        for key , value in freq.items():
            if value > n//2:
                return key
    def majority_element_optimized_approach(self , nums:List[int]) -> int:
        count = 0
        element = 0
        n = len(nums)

        for num in nums:
            if count == 0:
                count += 1
                element = num
            elif element == num:
                count += 1
            else:
                count -= 1
            
        element_count = nums.count(element)

        if element_count > (n // 2):
            return element
        
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.majority_element_brute_approach([7, 0, 0, 1, 7, 7, 2, 7, 7]))
    print(sol.majority_element_optimized_approach([7, 0, 0, 1, 7, 7, 2, 7, 7]))