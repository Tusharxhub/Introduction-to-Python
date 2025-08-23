# Write a recursive function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

def gcd(a, b):
    # Base case: if b is 0, gcd is a
    if b == 0:
        return a
    else:
        # Recursive case: gcd(b, remainder of a/b)
        return gcd(b, a % b)

# Example usage
print(gcd(48, 18))  # Output: 6
print(gcd(56, 98))  # Output: 14
