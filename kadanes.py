def kadanes(arr):
    cur_sum = 0
    max_sum = float('-inf')
    start = 0
    end = 0
    temp_start = 0
    n = len(arr)
    for i in range(n):
        cur_sum += arr[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
            start = temp_start
            end = i
        if cur_sum < 0:
            cur_sum = 0
            temp_start = i + 1
    return (start, end)



arr = [20 , -10 , 15, 20 , 17, -20 , 10]
result = print(kadanes(arr))
