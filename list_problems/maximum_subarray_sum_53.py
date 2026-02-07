from typing import List
class Solution:
    def maxSubArray_brute_approach(self, nums: List[int]) -> int:

        max_sum = float('-inf')

        for i in range(len(nums)):

            for j in range(i,len(nums)):
                sum = 0
                for k in range(i , j+1):
                    sum += nums[k]
                max_sum = max(sum , max_sum)
        return max_sum
    
    def maxSubArray_optimal_apprach(self, nums: List[int]) -> int:

        '''
        Docstring for maxSubArray_optimal_apprach ( kadane's algorithm)
        
        :param self: 
        :param nums: list of numbers
        :type nums: int
        :return: Maximum subarray sum
        :rtype: int

        --> Using two variable max_sum  and sum. Sum stores the current sum and max sum is what i am returning from the function 

        '''
        max_sum = float('-inf')
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

            # If sum is greater then max_sum, that means we got the new maximum_sum 
            if sum > max_sum:
                max_sum = sum
            
            # if the sum is negative then we make sum = 0
            if sum < 0:
                sum = 0
        
        return max_sum
    



if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray_brute_approach([2, 3, 5, -2, 7, -4]))
    print(sol.maxSubArray_brute_approach([-2, -3, -7, -2, -10, -4]))
    print(sol.maxSubArray_optimal_apprach([-2, -3, -7, -2, -10, -4]))


        