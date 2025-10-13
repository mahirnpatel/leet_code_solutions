class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        charNumberDic = {i: chr(64 + i) for i in range(1,27)}
        
        if columnNumber <= 26:
            return charNumberDic[columnNumber]
        else:
            column_title = ""
            # quotient = 0
            # quotient = columnNumber // 26
            # column_title = column_title + charNumberDic[quotient]
            # rem = columnNumber % 26
            # column_title = column_title + charNumberDic[rem]
            
            while(columnNumber != 0):
              column_title = column_title + charNumberDic[columnNumber % 26]
              print(column_title)
              columnNumber = columnNumber // 26
                
           
            return column_title
               
def main():
    sol = Solution()
    print(sol.convertToTitle(701))
    print(sol.convertToTitle(28))
    
    
if __name__ == "__main__":
    main()