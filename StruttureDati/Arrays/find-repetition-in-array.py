array1 = [1, 2, 3, 1]

array2 = [1, 2, 3, 4]

array3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


def findDuplicate(arr):
    cache = {}
    for i in arr:
        if i in cache:
            return True
        cache[i] = i
    return False


print(f'array1: {findDuplicate(array1)}')

print(f'array2: {findDuplicate(array2)}')

print(f'array3: {findDuplicate(array3)}')