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

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2

    arr_a = arr[:mid]
    arr_b = arr[mid:]

    arr_a = merge_sort(arr_a)
    arr_b = merge_sort(arr_b)


    return merge(arr_a,arr_b)

G = [38,27,43,3,9,82,10]

print("Array G before sorting.")
print(G)

print("Array G after sorting.")
print(merge_sort(G))
