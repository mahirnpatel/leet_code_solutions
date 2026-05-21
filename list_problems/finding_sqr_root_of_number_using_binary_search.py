def finding_sqr_root(n) -> int:
    low = 0
    high = n // 2
    
    while low <= high:
        
        mid = (low + high) // 2
   
        mid += 1
        sqr = mid ** 2
       
        if sqr <= n:
            return mid + 1
        
        elif sqr > n:
            high = mid - 1
        
        else:
            low = mid + 1


print(finding_sqr_root(27))
print(finding_sqr_root(36))
print(finding_sqr_root(28))
    
    