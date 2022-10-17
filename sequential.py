
## sequential Search
def sequential_search(list,value):
    for i in range (len(list)):
        if value==list[i]:
            return i 
    return -1

def main():
    list =[1,2,3,4,5,6,7,8,9]
    value = 5
    print(sequential_search(list,value))
    print(Binary(list,value))
main() 