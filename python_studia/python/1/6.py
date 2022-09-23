list1 = [1,2,3,4,5,5,6,7,8,8,8,8,9,10,7,5,4,3,3,2,1]

for x, index in enumerate(list1):
     if (index+1 < len(list1)):
        if list1[index] == list1[index+1]:
            list1.pop(index+1)
    
print(list1)
