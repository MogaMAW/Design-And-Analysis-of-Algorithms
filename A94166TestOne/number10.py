

## sequential Search
# sequential Search has its worst case complexity as O(n)
def sequential_search(list,value):    # O(1)
    for i in range (len(list)):   # the for loop takes O(n)
        if value==list[i]:       # O(1)
            return i 
    return -1

def main():           # O(1)
    list =[1,2,3,4,5,6,7,8,9]    # O(1)
    value = 9          # O(1)
    print(sequential_search(list,value))   # O(1)
    print((list,value))    # O(1)
main()      # O(1)


# the worst time complexity of the above sequential search is O(n)
# sequential search is at worst case complexity when either the last element was the element being searched for or when the element being searched for is not in the list
#in the above program we are searching for element 9 which is at index 8 and is the last element thus worst case 