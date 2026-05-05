from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> int:
        def binary_search(nums: List[int], target: int, left_most: bool) -> int:
            low = 0
            high = len(nums) - 1
            idx = -1
            while low <= high:
                mid = (low + high) // 2
                #When match found, save the index and move to the right to find the last position
                if nums[mid] == target:
                    idx = mid
                    if left_most:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif target < nums[mid]: #When target is less then move left
                    high = mid - 1
                else:
                    low = mid + 1 #Otherwise move right
            return idx
        left_most = binary_search(nums, target, True)
        right_most = binary_search(nums, target, False)
        return [left_most, right_most]
                
def main():
    sol = Solution()
    print(sol.searchRange([5,7,7,8,8,10], 8))
    print(sol.searchRange([5,7,7,8,8,10], 6))
    print(sol.searchRange([3, 4, 13, 13, 13, 20, 40], 13))
    print(sol.searchRange([3, 4, 13, 13, 13, 20, 40], 60))

if __name__ == "__main__":
    main()