a = 3
b = 10


def modular_recursive_Exponential(a, b, m):
    if b == 0:
        return 1
    elif b % 2 == 0:  # n is even
        return(modular_recursive_Exponential((a*a) % m, b/2, m))
    else:  # n is odd
        return(a*modular_recursive_Exponential((a*a) % m, b/2, m)) % m

    # Time Complexity O(log N)
    # Space Complexity O(log N)


def modular_iterative_exponential(a, b, m):
    result = 1
    while b > 0:
        if b % 2 == 1:  # odd
            result = (result * a) % m
        a = (a*a) % m
        b = b/2
    return result

    # Time Complexity O(log N)
    # space Complexity O(1)
