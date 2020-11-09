# Selection sort involves finding the minimum element in one pass through the array
# and then swapping it with the first position of the unsorted part of the array.
# Time complexity of selection sort is O(n^2) in all cases

def selection_sort(array):
    iteration_count = 0
    for i in range(len(array)-1):
        print(array)
        minimum = array[i]
        minimum_index = i
        for j in range(i + 1, len(array)):
            iteration_count += 1
            if array[j] < minimum:
                minimum = array[j]
                minimum_index = j
        if minimum_index != i:
            array[minimum_index], array[i] = array[i], array[minimum_index]
    return f'{array} \nAnd the number of iteration is {iteration_count}'


array = [5, 9, 3, 3, 10, 45, 2, 0]
print(selection_sort(array))
