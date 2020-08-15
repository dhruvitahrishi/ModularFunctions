# gcd of number is the largest positive number that divides both the number
def basic_gcf(a, b):
    m = min(a, b)
    gcd = 1
    i = m
    while i > 0:
        if(a % i == 0 and b % i == 0):
            gcd = i
            return gcd
        i -= 1
    return gcd

    # Time Complexity O(min(a,b))
