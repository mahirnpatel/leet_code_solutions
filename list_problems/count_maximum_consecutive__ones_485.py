def count_maximum_ones(arr):
    count = 0
    maxi = -1
    
    for i in arr:
        if i == 1:
            count += 1
        else:
            count = 0
        
        maxi = max(maxi, count)
            
    return maxi

print(count_maximum_ones([1,1,0,1,1,1]))