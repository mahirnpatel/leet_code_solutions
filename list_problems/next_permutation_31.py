from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #Step 1 find the drop 
        n = len(nums)
        index = -1
        for i in range(n-2 , -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break
        
        # If index == -1 means there is no drop in the array so we can just reverse the original array
        if index == -1:
            nums.reverse()
            
        else:
            #Swap the index element wit the largest element found in the sliced array    
            for i in range(n-1 , index , -1):
                if nums[i] > nums[index]:
                    nums[index]  , nums[i] = nums[i] , nums[index]
                    break
            
            nums[index + 1:] = nums[index + 1:][::-1]
        

        print(nums)

if __name__ == "__main__":
    sol = Solution()
    sol.nextPermutation([1,3,2])
    sol.nextPermutation([3,2,1])

        
        
