# Create a generator function fibonacci_sequence that yields an infinite Fibonacci sequence. Write a loop to print the first 20 numbers from this sequence.

def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Print the first 20 Fibonacci numbers
if __name__ == "__main__":
    fib_gen = fibonacci_sequence()
    for _ in range(20):
        print(next(fib_gen))