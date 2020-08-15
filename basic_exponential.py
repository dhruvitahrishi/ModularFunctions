import math
# to find a^b in optimised method
a = 3
b = 10


def iterativeExponential(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = result*a
        a = a*a
        b = int(b/2)
    return result


def recursiveExponential(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        #b is even
        return recursiveExponential(a*a, b/2)
    else:
        # b is odd
        return a * recursiveExponential(a*a, (b-1)/2)


print("Recursive: " + str(recursiveExponential(a, b)))

print("Iterative: " + str(iterativeExponential(a, b)))

# these functions would compute the exact answers but it will produce garbage values
# It might also be an issue to store this answers
# in over to avoid that use modular exponential in those lines
#  where temporary answers are computed.

