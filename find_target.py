def find_target(target, array):
    results = []
    i = 0
    while i < len(array):
        first = array[i]
        for ele in array[i+1:]:
            if (ele + first) == target:
                results.append(array.index(first))
                results.append(array.index(ele))
        
        i += 1
    
    return results
    
    
    
print(find_target(9, [2, 7,11,15])) # Result should == [0, 1]  
print(find_target(6, [3,2,4])) # Result should == [1, 2]
