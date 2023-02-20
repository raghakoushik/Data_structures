arr = [5,8,3,9,4,1,7]


#print(arr)

#print(range(len(arr)))


for i in range(len(arr)):

    #print(i)
    #minvalue = arr[i]
    minindex = i

    for j in range(i+1,len(arr)):
        #print(j)
        if arr[j] < arr[minindex]:
            #minvalue = arr[j]
            minindex = j
    (arr[i], arr[minindex]) = (arr[minindex], arr[i])

print(arr)