def findMaxMin(arr, i, j):
    if i == j:
        return arr[i], arr[i]
    elif i == j - 1:
        if arr[i] < arr[j]:
            return arr[i], arr[j]
        else:
            return arr[j], arr[i]
    else:
        mid = (i + j) // 2
        min1, max1 = findMaxMin(arr, i, mid)
        min2, max2 = findMaxMin(arr, mid + 1, j)
        return min(min1, min2), max(max1, max2)

arr = [20, 35, 95, 19, 105, 117, 17]
result = findMaxMin(arr, 0, len(arr) - 1)
print("Min:", result[0], "Max:", result[1])
