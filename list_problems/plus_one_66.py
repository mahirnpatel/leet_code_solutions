from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       number = int("".join(map(str, digits))) + 1
       digits = [int (i) for i in str(number)]
       return digits
  
def main():
    sol = Solution()
    print(sol.plusOne([1,2,3]))
    print(sol.plusOne([4,3,2,1]))
    print(sol.plusOne([1,9]))
    print(sol.plusOne([9,9]))
    print(sol.plusOne([9]))
    
    
    
    

    
if __name__ == "__main__":
    main()