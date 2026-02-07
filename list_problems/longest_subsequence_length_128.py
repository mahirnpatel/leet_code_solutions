from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 0:
            return 0
        
        longest = 1
        st = set()

        for num in nums:
            st.add(num)
        
        for i in st:

            if i - 1 not in st:

                counter = 1

                current = i

                while current + 1 in st:
                    counter += 1
                    current += 1
                
                longest = max(longest , counter)

        return longest
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,1,2]))