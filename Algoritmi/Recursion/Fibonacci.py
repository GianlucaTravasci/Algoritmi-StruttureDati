def iterative_fibonacci(index):
    first = 0
    second = 1
    if index == 0:
        return first
    if index == 1:
        return second
    for i in range(2, index + 1):
        third = first + second
        first = second
        second = third
    return third


print("Iterative fibonacci:")
print(iterative_fibonacci(0))  # 0
print(iterative_fibonacci(1))  # 1
print(iterative_fibonacci(5))  # 5
print(iterative_fibonacci(7))  # 13
print(iterative_fibonacci(10))  # 55
print(iterative_fibonacci(12))  # 144
print(" ")


def recursive_fibonacci(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    return recursive_fibonacci(index - 1) + recursive_fibonacci(index - 2)


print("recursive fibonacci:")
print(recursive_fibonacci(0))  # 0
print(recursive_fibonacci(1))  # 1
print(recursive_fibonacci(5))  # 5
print(recursive_fibonacci(7))  # 13
print(recursive_fibonacci(10))  # 55
print(recursive_fibonacci(12))  # 144
