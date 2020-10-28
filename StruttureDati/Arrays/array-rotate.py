# from right to left
def rotateArrayByOneToLeft(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i + 1]
    arr[len(arr)-1] = temp

# from left to right
def rotateArrayByOneToRight(arr):
    temp = arr[len(arr)-1]
    for i in reversed(range(len(arr)-1)):
        arr[i+1] = arr[i]
    arr[0] = temp

def rotateArrayForNTimes(arr, num):
    for index in range(num):
        rotateArrayByOneToLeft(arr)



array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

rotateArrayByOneToLeft(array1)

rotateArrayByOneToRight(array2)

rotateArrayForNTimes(array1, 5)

rotateArrayForNTimes(array2, 5)

print(array1)

print(array2)