def factorial_recursive(num):
    answare = 1
    if num != 0:
        answare = num * factorial_recursive(num - 1)
    return answare


def factorial_iterative(num):
    answare = 1
    for i in range(1, num+1):
        answare *= i
    return answare


print(factorial_recursive(10))
print(factorial_iterative(10))
