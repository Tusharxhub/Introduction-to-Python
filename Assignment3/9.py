# Convert a decimal number to its binary representation without using built-in functions.

def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def main():
    print("--- Decimal to Binary Converter ---")
    decimal_number = int(input("Enter a decimal number: "))
    binary_representation = decimal_to_binary(decimal_number)
    print(f"Binary representation of {decimal_number} is: {binary_representation}")

if __name__ == "__main__":
    main()
