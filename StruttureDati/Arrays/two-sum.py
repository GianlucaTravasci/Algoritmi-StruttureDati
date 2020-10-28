input = [2, 7, 11, 15]
sum = 9

def twoSum(arr, target):
    cache = {}
    for i in range(len(arr)):
        if target-arr[i] in cache:
            return [cache[target-arr[i]], i]
        else:
            cache[arr[i]] = i
print(twoSum(input, sum))