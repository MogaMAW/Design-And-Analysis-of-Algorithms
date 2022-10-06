
A = [1,2,3,6,8]
x=1
print("Array z before sorting.")
print(A)
print(len(A))


while x < len(A):
    key= A[x]

    y=x-1
    while y>=0 and A[y]> key:
        A[y+1] = A[y]

        y=y-1
    A[y+1] = key
    
    x=x+1

print(A)
