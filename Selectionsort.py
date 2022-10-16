def Selection(list):
    n =len(list)
    for i in range(0,n-1):
        mini=i
        for j in range((i+1),n):
            if list[mini]>list[j]:
                #list[mini],list[j]=list[j],list[mini]
                mini=j
                if mini!=1:
                    list[mini],list[i] = list[i],list[mini]
def main():
    list=[3,9,7,3,2,4,6,3,7,8]
    print(list)
    Selection(list)
    print(list)
main() 
                