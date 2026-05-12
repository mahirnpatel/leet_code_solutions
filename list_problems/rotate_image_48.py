from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # for row in matrix:
        #     print(row)
        
        matrix = [list(row) for row in zip(*matrix)]
        # print('----After transpose----')
        # for row in matrix:
        #     print(row)
        low = 0
        high = len(matrix)-1

        while low < high:
            # matrix[low], matrix[high] = matrix[high] , matrix[low]
            for row in range(len(matrix)):
                matrix[row][low],matrix[row][high] = matrix[row][high],matrix[row][low]
            low += 1
            high -= 1

        # print('----After rotation----')
        # for row in matrix:
        #     print(row)
        print(matrix)


if __name__ == "__main__":
    sol =Solution()
    sol.rotate( [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]])
    sol.rotate( [[1,2,3],[4,5,6],[7,8,9]])
    sol.rotate( [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])

        