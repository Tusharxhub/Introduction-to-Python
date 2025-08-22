# Write a Python decorator timer that measures the execution time of a function and prints the result. Apply this decorator to a function that performs a complex calculation, such as finding prime numbers up to a given limit.


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()   # Record start time
        result = func(*args, **kwargs)  # Run the function
        end_time = time.time()     # Record end time
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

@timer
def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

if __name__ == "__main__":
    primes = find_primes(10000)
    print(f"Found {len(primes)} prime numbers up to 10000.")
