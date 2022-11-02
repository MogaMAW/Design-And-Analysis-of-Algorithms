"""
Find the min and max that can be calculated by summing the four of the five integers
we are going to use an array

We are using an array of values [4, 3, 1, 6, 7]

"""
from merge_sort import merge_sort
from reversed_merge_sort import reverse_merge_sort


def O2N(arr):
    pivot_big = arr[0]
    pivot_small = arr[0]
    sum = 0

    for value in range(len(arr)):
        if arr[value] > pivot_big:
            pivot_big = arr[value]
        elif arr[value] < pivot_small:
            pivot_small = arr[value]
    
    for el in arr:
        sum += el
    
    small_ones = sum - pivot_big
    big_ones = sum - pivot_small

    return f"{small_ones} {big_ones}"
    

# arr = [4, 3, 1, 6, 7]
# print(O2N(arr))



"""To help us sum the values in our arrays"""
def sums(sorted_arr):
    if len(sorted_arr) >= 4:
       return sorted_arr[0] + sorted_arr[1] + sorted_arr[2] + sorted_arr[3]
  

def NlogN(arr):
    sorted_arr = merge_sort(arr) #[1, 3, 4, 6, 7] 
    rev = sorted_arr[::-1]

    sumS = sums(sorted_arr)
    sumB = sums(rev)

    return f"{sumS} {sumB}"

# arr = [4, 3, 1, 6, 7]
# print(NlogN(arr))

def fn_2NlogN(arr):
    sorted_arr_asc = merge_sort(arr)
    sumS = sums(sorted_arr_asc)

    sorted_arr_desc = reverse_merge_sort(arr)
    sumB = sums(sorted_arr_desc)

    return f"{sumS} {sumB}"

arr = [4, 3, 1, 6, 7]
print(fn_2NlogN(arr))


    





