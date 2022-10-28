def merge(a,b):       # O(1)
    sorted_arr = []    # O(1)

    x = 0
    y = 0

    len_a = len(a)
    len_b = len(b)
    while x < len_a and y < len_b:      # the while loop takes O(n)
        if a[x] <= b[y]:                #the if statement takes O(1)
            sorted_arr.append(a[x])       # O(1)
            x=x+1                           # O(1)
        else:
            sorted_arr.append(b[y])            # O(1)

            y=y+1                                # O(1)
    while x < len_a:                                 # While loop takes O(n) since it is not nested
        sorted_arr.append(a[x])                      # O(1)
        x=x+1                                        # O(1)

    while y < len_b:                             # while loop takes O(n) since it is not nested
        sorted_arr.append(b[y])                  # O(1)
        y=y+1                                    # O(1)

    return sorted_arr                                # O(1)

def merge_sort(arr):
    if len(arr) <= 1: #to check if the list has elements in it.   O(1)
        return arr       # O(1)
    
    mid = len(arr)//2  # finding the mid of the array

    arr_a = arr[:mid]        # O(1)
    arr_b = arr[mid:]        # O(1)
 
    arr_a = merge_sort(arr_a)       # O(1)
    arr_b = merge_sort(arr_b)     # O(1)


    return merge(arr_a,arr_b)       # O(1)

G = ["Solomon","Daphine","Charles","Tracy", "Jasper", "Destiny","Nabil"]

print("Array G before sorting.")
print(G)

print("Array G after sorting.")
print(merge_sort(G))


#complexity of the Merge sort is: O(n) + O(n) + O(n) = O(3n)

# The complexity of this Merge Sort Method is O(n)