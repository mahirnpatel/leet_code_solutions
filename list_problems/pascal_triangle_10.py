from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[List[int]]:
        pascal_list = [[1],[1,1]]
        counter = 1
        if rowIndex == 0:
            return pascal_list[0]
        if rowIndex == 1:
            return pascal_list[1]
            
        for i in range(rowIndex - 1):
            p_list = []
            for j in range(len(pascal_list[counter])-1):
                if j == 0:
                   p_list.append(1)
                p_list.append(pascal_list[counter][j] + pascal_list[counter][j+1])
            p_list.append(1)
            pascal_list.append(p_list)
            counter +=1
        return pascal_list[rowIndex]
    
def main():
    sol = Solution()
    print(sol.generate(3))

if __name__ == '__main__':
    main()