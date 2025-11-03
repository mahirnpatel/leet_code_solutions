from collections import Counter
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        most_common , _ = freq.most_common(1)[0]
        return(most_common)

def main():
    sol = Solution()
    print(sol.majorityElement([3,2,3]))
    print(sol.majorityElement([2,2,1,1,1,2,2]))
    
if __name__ == '__main__':
    main()