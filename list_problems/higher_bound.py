from typing import List

class Solution:
    def higher_bound_linear_search(self, arr: [int] , target: int) -> int:
        for i in range(len(arr)):
            if arr[i] > target:
                return i 
        return len(arr)

def main():
    sol = Solution()
    print(sol.higher_bound_linear_search([10,20,30,40,50] , 30))

if __name__ == "__main__":
    main()
                