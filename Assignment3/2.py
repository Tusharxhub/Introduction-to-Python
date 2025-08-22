# 2.	Write a program that takes a range of numbers (e.g., 1 to 100) and prints all the prime numbers within that range.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Print all prime numbers in the range 1 to 100
for n in range(1, 101):
    if is_prime(n):
        print(n)
