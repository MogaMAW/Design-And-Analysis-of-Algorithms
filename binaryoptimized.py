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

