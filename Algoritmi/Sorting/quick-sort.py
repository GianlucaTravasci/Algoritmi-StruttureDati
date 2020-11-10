# Quick Sort is another sorting algorithm which follows divide and conquer approach. It requires to chose a pivot,
# then place all elements smaller than the pivot on the left of the pivot and all elements larger on the right Then
# the array is partitioned in the pivot position and the left and right arrays follow the same procedure until the
# base case is reached. After each pass the pivot element occupies its correct position in the array. Time Complexity
# in Best and Average cases is O(nlog N) whereas in worst case it jumps up to O(n^2). Space complexity is O(log n)


def quicksort(array, left, right):
    if left < right:
        pivot = right
        partition_index = partition(array, pivot, left, right)

        quicksort(array, left, partition_index - 1)
        quicksort(array, partition_index + 1, right)
    return array


def partition(array, pivot, left, right):
    pivot_value = array[pivot]
    partition_index = left

    for i in range(left, right):
        if array[i] < pivot_value:
            swap(array, i, partition_index)
            partition_index += 1

    swap(array, right, partition_index)
    return partition_index


def swap(array, first_index, second_index):
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(quicksort(numbers, 0, len(numbers) - 1))
