from typing import List
class Solution:
    def lower_bound_linear_search(self, arr: List[int], target: int) -> int:
        for i in range(0, len(arr)):
            if arr[i] >= target:
                return i

        return len(arr)
    

    def lower_bound_binary_search(self, arr: List[int], low: int , high: int , target: int) -> int:
        while low <= high:
            mid = (low + high) // 2
            ans = len(arr)
            
            if target == arr[mid]:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            return ans
            
def main():
    sol = Solution()
    print(sol.lower_bound_linear_search([10,20,30,40,50], 30))
    print(sol.lower_bound_binary_search([10,20,30,40,50], 0 , 4 , 30))

if __name__ == "__main__":
    main()