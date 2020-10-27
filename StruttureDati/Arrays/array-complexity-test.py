array1 = [1, 2, 3, 4, 5, 6]
array2 = [23, 7, 8, 9]

def findMatch(arr1, arr2):
    bag = {}
    for v in arr1: # O(n)
        if not v in bag:
            bag[v] = v

    for v in arr2: # O(n)
        if v in bag:
            return True
    return False

def findMatchBruteForce(arr1, arr2):
    for v1 in arr1:
        for v2 in arr2:
            if v1 == v2:
                return True
    return False

print(findMatch(array1, array2)) # O(n)

print(findMatchBruteForce(array1, array2)) # O(n^2)