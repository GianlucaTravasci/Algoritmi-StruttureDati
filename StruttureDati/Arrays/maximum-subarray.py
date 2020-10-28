def maxSubArray(arr):
    max_so_far = arr[0]
    current_max = arr[0]

    for i in range(1, len(arr)-1):
        current_max = max(arr[i], current_max + arr[i])
        max_so_far = max(max_so_far, current_max)

    return max_so_far

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maxSubArray(a))