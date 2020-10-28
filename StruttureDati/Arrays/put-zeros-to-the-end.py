# Function that push all the zeros to the end of an array

def pushToTheEnd(arr):
    count = 0
    for index in range(len(arr)):
        if arr[index] != 0:
            arr[count] = arr[index]
            count += 1
    while count < len(arr):
        arr[count] = 0
        count += 1


array=[1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
pushToTheEnd(array)
print(array)