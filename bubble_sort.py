def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]> arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
    return arr


# driver code
arr = [64, 34, 25, 12, 22, 11, 90]
result = bubble_sort(arr)
print("Sorted array is:", result)