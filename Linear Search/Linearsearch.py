def linearUnsorted(list,value):
    for i in range(len(list)):
        if value == list[i]:
            return i
     
    return -1

def main():
    list=[6,9,5,3,7,3,2]
    value = 3
    print(linearUnsorted(list,value))
main()