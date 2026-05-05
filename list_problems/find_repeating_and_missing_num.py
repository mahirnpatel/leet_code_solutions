def find_repeating_and_missing_num(nums):
    n = len(nums)
    s = set(nums)
    max_element = max(nums)
    n_sum = max_element * (max_element + 1) // 2
    result = []
    original_sum = sum(s)
    list_sum = sum(nums)
    result.append(list_sum - original_sum)
    result.append( n_sum - original_sum)
    print(result)
   

find_repeating_and_missing_num([3,5,4,1,1])
find_repeating_and_missing_num([1, 2, 3, 6, 7, 5, 7]  
)
    