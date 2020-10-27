array1 = [1, 2, 3, 4, 5, 6]
array2 = [2, 7, 8, 9]

def copyArrayIntoACache(array):
    cache = {}
    for v in array: # O(n)
        if not v in cache:
            cache[v] = v

    return cache

def compareArrayAndCache(cache, array):
    for value in array:
        if value in cache:
            return True
    return False

def findMatch(arr1, arr2):
    if arr1 and arr2:
        cache = copyArrayIntoACache(arr1)
        result = compareArrayAndCache(cache, arr2)
        return result

    return 'something is missing'



#def findMatchBruteForce(arr1, arr2):
    #for v1 in arr1:
        #for v2 in arr2:
            #if v1 == v2:
                #return True
    #return False

print(findMatch(array1, array2)) # O(n)

# print(findMatchBruteForce(array1, array2)) # O(n^2)