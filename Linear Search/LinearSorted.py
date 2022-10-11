def LinearwhenSorted(list,value):
    for i in range(len(list)):
        if value == list[i]:
            return True
        else: list[i]>value
    return False 
def main():
    list=[1,2,3,4,5,6,7,8]
    value = 4
    print(list)
    print(LinearwhenSorted(list,value))
    
main()
        
            