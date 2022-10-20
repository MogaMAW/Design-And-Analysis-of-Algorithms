
#class work assignment 
#1. Merge sort optimization to stop dividing sub-arrays when one side of the array is already sorted

G = [38,27,43,3,9,82,10]
def merge_sort(arr):
    Test_check =0
    i=1
    
    if len(arr) <= 1: #to check if the list has elements in it.
        return arr
    while i < len(arr):
        if(arr[i]<arr[i-1]):
            red_flag =1
        i +=1
    if(not Test_check):
        return arr
    else :
        mid = len(arr)//2

        arr_a = arr[:mid]
        arr_b = arr[mid:]

        arr_a = merge_sort(arr_a)
        arr_b = merge_sort(arr_b)
        print(arr_a)
        print(arr_b)


        return merge(arr_a,arr_b)
    
def merge(a,b):
    sorted_arr = []

    x = 0
    y = 0

    len_a = len(a)
    len_b = len(b)
    while x < len_a and y < len_b:
        if a[x] <= b[y]:
            sorted_arr.append(a[x])
            x=x+1
        else:
            sorted_arr.append(b[y])

            y=y+1
    while x < len_a:
        sorted_arr.append(a[x])
        x=x+1

    while y < len_b:
        sorted_arr.append(b[y])
        y=y+1

    return sorted_arr
print(merge_sort(G))


#2.
#Bubble
#optimized buble sort: so that when a sorted array is given, it does not do alot of iterations or comparisons

def bubblesort(list):
    k = len(list)
    for i in range(k-1):
        sort_status = False
        for j in range((k-1)-i):
            if list[j]> list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                sort_status = True
        if  not sort_status:
            break
    return list
list=[2,6,4,3]
bubblesort(list)
print(list)
# #  Best Case:O(n) 
# # Worst Case: O(n^2)


# #3.
# #The Binary search class
def division(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quickSort(array, low, high):
    if low < high:

        div = division(array, low, high)

    quickSort(array, low, div - 1)

    quickSort(array, div + 1, high)

data = [4,1,2,3]

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array is:')
print(data)

def binary_search(array1, search_val):
    begin = 0
    end = len(array1)-1

    while begin <= end:
        middle = int((begin + end)/2)

        if search_val == array1[middle]:
            return True

        elif search_val == array1[middle]:
            end = middle-1

    else:
        begin = middle + 1

    return False

input_sequence = data
search_val1 = 4

print(binary_search(input_sequence, search_val1))

