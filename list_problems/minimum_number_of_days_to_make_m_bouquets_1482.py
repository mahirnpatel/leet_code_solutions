from typing import List
class Solution:
    def is_possible(self, bloom_day, day, m , k):
        count = 0
        bouquet = 0
        
        for bloom in bloom_day:
            if bloom <= day:
                count += 1
                if count == k:
                    bouquet += 1
                    count = 0
            else:
                count = 0
            
        if bouquet >= m:
            return True
        else:
            return False
        
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        low = min(bloomDay)
        high = max(bloomDay)
        answer = -1 
        
        while low <= high:
            mid = (low + high) // 2
            
            if (self.is_possible(bloomDay , mid, m , k)):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer


def main():
    sol = Solution()
    print(sol.minDays([1,10,3,10,2], 3 , 1))
    print(sol.minDays([1,10,3,10,2], 3 , 2))
    print(sol.minDays([7,7,7,7,12,7,7], 2 , 3))

if __name__ == "__main__":
    main()