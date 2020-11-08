def iterative_reverse(string):
    reversed_str = ""
    for i in range(len(string)):
        reversed_str += string[len(string)-i-1]
    return reversed_str


print(iterative_reverse("something"))


def recursive_reverse(string):
    if len(string) == 0:
        return string
    else:
        return recursive_reverse(string[1:]) + string[0]


print(recursive_reverse("something"))