def Bubble(list):
    n = len(list)
    for i in range(0,(n-1)):
        for j in range((n-i)-1):
            if list[j] > list[j+1]:
                list[j+1],list[j] = list[j],list[j+1]

def main():
    list = [9,4,6,7,2,4,5]
    print(list)
    Bubble(list)
    print(list)
main()