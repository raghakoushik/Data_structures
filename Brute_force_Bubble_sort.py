arr = [5, 8, 3, 9, 4, 1, 7]


for i in range(len(arr)):
    #print(i)
    for j in range(len(arr)-1,i,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]

print(arr)



