from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and target <= nums[0]:
            return 0
        else: 
            for i in range(0,len(nums)-1):
                if target <= nums[0]:
                    return 0
                elif nums[i] == target:
                    return i
                elif nums[i] <= target and nums[i+1] >= target:
                    return i+1
        return len(nums)

    def searchInsert_binary_search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        ans = len(nums)
        while low <= high:
            mid = (low + high) // 2
            if target >= nums[mid]:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
    
def main():
    sol = Solution()
    print(sol.searchInsert([1,3],3))
    print(sol.searchInsert_binary_search([1,2,4,5,7],6))
    print(sol.searchInsert_binary_search([1,3,5,6],5))
if __name__ == '__main__':
    main()