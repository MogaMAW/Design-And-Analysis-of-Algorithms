array =[172,11,423,172,30,910,172,9,2,45,60,172]

def Linearsearch(array, x):
 
    for i in range(len(array)):
 
        if array[i] == x:
            return i
 
    return -1
print(Linearsearch(array,172))

def worstcase(a,value):
    z =[]
    for i in range(len(a)):
        if array[i] == value:
            z.append(i)
            
    return z 
print(worstcase(array,172))
