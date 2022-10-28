
#Quick sort's average case time complexity is O(n*logn)
#Quick sort's best case time complexity is: O*log(n) when the partitions are as evenly balanced as possible

#Worst Case Complexity:  n^2 is when the algortihm pick the largest or smallest element as the pivot element every time.
#worst case is when the elements are sorted, reversed sorted or all elements are same


def quickSort(data_list):
   quickSortHlp(data_list,0,len(data_list)-1)

def quickSortHlp(data_list,first,last):
   if first < last:

       splitpoint = partition(data_list,first,last)

       quickSortHlp(data_list,first,splitpoint-1)
       quickSortHlp(data_list,splitpoint+1,last)


def partition(data_list,first,last):
   pivotvalue = data_list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and data_list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while data_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = data_list[leftmark]
           data_list[leftmark] = data_list[rightmark]
           data_list[rightmark] = temp

   temp = data_list[first]
   data_list[first] = data_list[rightmark]
   data_list[rightmark] = temp


   return rightmark

data_list = [25,29,30,35,42,47,50,52,60]
quickSort(data_list)
print(data_list)
 
