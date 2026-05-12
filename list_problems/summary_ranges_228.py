from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k = len(nums)
        original_sum = 0
        missing_sum = 0
        for i in range(0,k+1):
            original_sum = original_sum + i
            if i < k:
                missing_sum = missing_sum + nums[i]
        return original_sum - missing_sum
            
def main():
    sol = Solution()
    print(sol.missingNumber([3,0,1]))
    print(sol.missingNumber([0,1]))
    print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))

if __name__ == '__main__':
    main()