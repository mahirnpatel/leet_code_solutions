# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal1 = int(a , 2)
        decimal2 = int(b ,2)
        
        binary_sum = bin(decimal1 + decimal2)[2:]
        return binary_sum
        
def main():
    sol = Solution()
    print(sol.addBinary("11", "1"))
    

if __name__ == "__main__":
    main()
