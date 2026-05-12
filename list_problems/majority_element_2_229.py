from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter1 = 0
        counter2 = 0
        element1 = float('-inf')
        element2 = float('-inf')

        for num in nums:
            if counter1 == 0 and num != element2:
                counter1 += 1
                element1 = num

            elif counter2 == 0 and num != element1:
                counter2 += 1
                element2 = num
            elif num == element1:
                counter1 += 1

            elif num == element2:
                counter2 += 1
            else:
                counter1 -= 1
                counter2 -= 1
        # return [element1 , element2]

        #Validate the candidates 
        counter1 , counter2 = 0,0

        for num in nums:
            if num == element1:
                counter1 += 1
            if num == element2:
                counter2 += 1

        n = len(nums)
        mini = n // 3 + 1

        result = []

        if counter1 >= mini:
            result.append(element1)

        if counter2 >= mini and element1 != element2:
            result.append(element2)

        
        return result 
    
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([3,2,3]))
    
