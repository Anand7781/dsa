def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

# driver code
arr = [64, 34, 25, 12, 22, 11, 90]
result = insertion_sort(arr)
print("Sorted array is:", result)