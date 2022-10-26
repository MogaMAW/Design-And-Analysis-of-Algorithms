def binarySearch(array, target): #returns the index or the target 
    low = array[0]
    high = array[len(array)-1]
    if array[0] == target:
            return 0
    elif array[len(array)-1] == target:
        return len(array)-1
    else:
        while(low <= high):
            mid = int((low+high)/2)
            if array[mid]==target:
                return mid
            elif array[mid] > target:
                high = mid -1
            elif array[mid] < target:
                low = mid +1
        return -1  #returns -1 if the target does not exist

def main():
    array =[1,2,3,4,5,6,7,8]
    target= 3
    print(binarySearch(array, target))
main()