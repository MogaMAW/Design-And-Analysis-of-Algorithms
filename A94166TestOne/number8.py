
#Best case of a selection sort 
#Best case scenario of a selection sort is when the elements in the list are already in order or are sorted.
def Selection(list):
    n =len(list)
    for i in range(0,n-1):
        mini=i
        for j in range((i+1),n):
            if list[mini]>list[j]:
            
                mini=j
                if mini!=1:
                    list[mini],list[i] = list[i],list[mini]
def main():
    list=[3,4,5,6,7]
    print(list)
    Selection(list)
    print(list)
main() 

#worst case
#The worst case is when the array is completely unsorted or sorted in descending order.
def Selection(list):
    n =len(list)
    for i in range(0,n-1):
        mini=i
        for j in range((i+1),n):
            if list[mini]>list[j]:
            
                mini=j
                if mini!=1:
                    list[mini],list[i] = list[i],list[mini]
def main():
    list=[3,9,7,3,2,4,6,3,7,8]
    print(list)
    Selection(list)
    print(list)
main() 




                
