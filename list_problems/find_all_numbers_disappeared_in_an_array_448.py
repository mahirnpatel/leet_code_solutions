# from typing import List
class Solution:
    def findDisappearedNumbers(self, nums):
        s = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in s]
        
def main():
    sol = Solution()
    print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    sol.findDisappearedNumbers([1,1])

if __name__ == '__main__':
    main()
    