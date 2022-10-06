# Method 2 sorting array Z in descending order
def insertion_sort(Z):
    for x in range(1,len(Z)):
        value = Z[x]
        y = x-1

        while y>=0:
            if value >Z[y]:
                Z[y+1] = Z[y]
                Z[y] = value
                y = y-1
            else:
                break


Z = [20,35,45,10,40,60]
print("Array Z before sorting:")
print(Z)

insertion_sort(Z)
print("Array Z after sorting in decending order:")
print(Z)

