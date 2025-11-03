from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merged_list = []
        i = j = 0
        while(i < m and j < n):
            if nums1[i] <= nums2[j]:
                merged_list.append(nums1[i])
                i +=1
            else:
                merged_list.append(nums2[j])
                j +=1 
        merged_list.extend(nums1[i:m])
        merged_list.extend(nums2[j:n])
        nums1[:] = merged_list
        # print(nums1)

def main():
    sol = Solution()
    sol.merge([1,2,3,0,0,0],3,[2,5,6],3)
    
    sol.merge([1],1,[],0)
    sol.merge([0],0,[1],1)
if __name__ == "__main__":
    main()