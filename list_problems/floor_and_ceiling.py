from typing import List
class Solution:
    def floor(self, arr: List[int], target: int) -> int:
        low = 0
        high = len(arr) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= target:
                ans = arr[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans
    
    def ceiling(self, arr: List[int], target: int) -> int:
        low = 0
        high = len(arr) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                ans = arr[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans

def main():
    sol = Solution()
    print("Floor of 8 is: ", sol.floor([3,4,4,7,8,10], 8))
    print("Ceiling of 8 is: ", sol.ceiling([3,4,4,7,8,10], 8))
    print("Floor of 1 is: ", sol.floor([3,4,4,7,8,10], 1))
    print("Ceiling of 1 is: ", sol.ceiling([3,4,4,7,8,10], 1))

if __name__ == "__main__":
    main()
 