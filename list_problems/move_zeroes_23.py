from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        //Brute force approach
        moved_list = []
        zeroes = 0
        if len(nums) == 1 and nums[0] == 0:
            return [0]
        else:
            for i in range(len(nums)):
                if nums[i] > 0:
                    moved_list.append(nums[i])
                else:
                    zeroes = zeroes + 1
            moved_list = moved_list + [0] * zeroes
            nums = moved_list[:]
            print(nums)
            return nums
            '''
            
            #Optimized version 
            
        index_for_non_zero = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[index_for_non_zero] , nums[j] = nums[j], nums[index_for_non_zero]
                index_for_non_zero += 1

        return nums
def main():
    sol = Solution()
    print(sol.moveZeroes([0,1,0,3,12]))
    print(sol.moveZeroes([0]))

if __name__ == '__main__':
    main()
        