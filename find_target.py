def find_target(target, array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if target == array[i] + array[j]:
                return [i, j]
    
    
    
print(find_target(9, [2, 7,11,15])) # Result should == [0, 1]  
print(find_target(6, [3,2,4])) # Result should == [1, 2]
print(find_target(6, [3,3])) # Result should == [0, 1]
