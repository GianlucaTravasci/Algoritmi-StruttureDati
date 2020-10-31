array = [2, 5, 1, 3, 4]

def findRecur(arr):
    cache = {}
    for i in range(len(arr)):
        if arr[i] in cache:
            return arr[i]
        cache[arr[i]] = i

print(findRecur(array))