#An algorithm that  reverses an array
def reverse(array):
    size = len(array)
    for i in range(0,size//2):
        (array[i],array[size-i-1]) = (array[size-i-1],array[i])
    return array
def main():
    array = [2,6,9,10]
    print(reverse(array))
main()


