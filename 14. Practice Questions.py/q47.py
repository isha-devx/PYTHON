"""
Q.47
write a function power(base, exp) that returns base
raised to exp using a loop - no ** operator or pow()
allowed.
"""

def power(base,exp):
    result= 1
    for i in range(1, exp+1):
        result = result * base
    return result

power(2,3)
print(power(2,3))