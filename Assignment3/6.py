# Create a program that checks if a password meets certain criteria (e.g., minimum length, contains uppercase, lowercase, numbers, and special characters).

def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-+"
    for char in password:
        has_upper |= char.isupper(); has_lower |= char.islower(); has_digit |= char.isdigit(); has_special |= char in special_characters
    return has_upper & has_lower & has_digit & has_special

def main():
    print("--- Password Validator ---")
    password = input("Enter a password to validate: ")
    if is_valid_password(password):
        print("Password is valid.")
    else:
        print("Password is invalid.")

if __name__ == "__main__":
    main()