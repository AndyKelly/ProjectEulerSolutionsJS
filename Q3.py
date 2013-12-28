import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_factor_of(toDivide, toBeDivided):
    return toBeDivided % toDivide == 0

def next_prime(x):
    if x > 2:
        x += 2
        while not is_prime(x):
            x += 2
    else:
        #edge case: when passed 0, 1 or 2
        x += 1
    return x

divider = 2
remainder = 600851475143

while divider != remainder:
    if is_factor_of(divider, remainder):
        remainder = remainder / divider
    else:
        divider = next_prime(divider)
print remainder
