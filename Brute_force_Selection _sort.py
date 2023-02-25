arr = [5, 8, 3, 9, 4, 1, 7]

for i in range(len(arr)):
    minindex = i

    for j in range(i+1, len(arr)):

        if arr[j] < arr[minindex]:
            minindex = j
    (arr[i], arr[minindex]) = (arr[minindex], arr[i])
print(arr)
