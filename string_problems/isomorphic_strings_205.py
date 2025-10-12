class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map = {}
        
        for ch1, ch2 in zip(s,t):
            if not hash_map:
                hash_map[ch1] = ch2
            else:
                 if ch1 in hash_map:
                    if hash_map[ch1] != ch2:
                        return False
                 else:
                    if ch2 in hash_map.values():
                         return False
                    hash_map[ch1] = ch2
        return True
    
def main():
    sol = Solution()
    print(sol.isIsomorphic("foo" , "bar"))
    print(sol.isIsomorphic("egg" , "add"))
    print(sol.isIsomorphic("paper" , "title"))
    print(sol.isIsomorphic("badc" , "baba"))
    
if __name__ == "__main__":
    main()
    
    