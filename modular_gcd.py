# GCD(A,B) = GCD(B,A%B)
#   it will recurse until A%B=0

def modularGCD(a, b):
    if b == 0:
        return a
    else:
        return modularGCD(b, a % b)

    # Time Complexity :- O(log(max(a,b)))
