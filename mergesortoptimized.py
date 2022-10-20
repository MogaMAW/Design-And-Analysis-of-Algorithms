#merge_Sort()
def merge_Sort(list):
    if len(list)>1:
        integrityChek = 0
        i = 1
        while i < len(list):
            if list[i-1] > list[i]:
                integrityChek = 1
            i += 1
        if (not integrityChek):
            return list
        else:
            mid  = len(list)//2
            left = list[:mid]
            right = list[mid:]

            merge_Sort(left)
            merge_Sort(right)

            i = j = k = 0

            while i < len(left) and j< len(right):
                if left[i] < right[j]:
                    list[k] = left[i]
                    i+=1
                else:
                    list[k] =right[j]
                    j+=1
                k +=1
            while i< len(left):
                list[k] = left[i]   
                i+=1
                k+=1    

            while j< len(right):
                list[k] = right[j]   
                j+=1
                k+=1   
    return list
class BinarySearch:
    def __init__(self,list):
        self.list = list
        Test = 0
        i = 1
        while i < len(list):
            if list[i-1] > list[i]:
                Test = 1
            i += 1
        if (not Test):
            print(" The List is sorted") 
        else:
            print("List is not sorted")
            print("Sorting list")
            self.list = merge_Sort(self.list)
            print("List is sorted")
            print("List: {0}".format(self.list))
            print("")
    def binarySearch(self,item):
        first = 0
        last = len(self.list)-1
        found = False
        while first<=last and not found:
            midpoint = (first + last)//2
            if self.list[midpoint] == item:
                found = True
            else:
                if item < self.list[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
        return found

def main():
    #list1 = [4,1,2,3]
    list1 = [4,1,2,3]
    print("List: {0}".format(list1))
    print("")
    #sort list
    list1 = merge_Sort(list1)
    print ("List from merge_Sort:")
    print("List: {0}".format(list1))
    print("")
    #binary search
    lookfor = int(input("Enter a value for search: "))
    print("")
    binary = BinarySearch(list1)
    found = binary.binarySearch(lookfor)
    if found:
        print("Found")
    else:
        print("Not found")
main()
