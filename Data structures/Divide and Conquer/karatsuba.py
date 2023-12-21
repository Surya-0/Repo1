def karatsuba(x, y):
    # Base case for small inputs
    if x < 10 or y < 10:
        return x * y

    # Calculate the size of the numbers
    m = min(len(str(x)), len(str(y)))
    m2 = m // 2

    # Split the input numbers into two halves
    high1, low1 = divmod(x, 10**m2)
    high2, low2 = divmod(y, 10**m2)

    # Recursively compute three products
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    # Use the three products to calculate the final result
    return (z2 * 10**(2 * m2)) + ((z1 - z2 - z0) * 10**m2) + z0

# Example usage:
x = 1234
y = 5678
result = karatsuba(x, y)
print(f"The product of {x} and {y} is: {result}")
# x,y = divmod(122,10)
# print(x," ",y)