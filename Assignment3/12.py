# Given a string and a character, remove all occurrences of that character from the string.
def remove_character(s: str, char_to_remove: str) -> str:
    return s.replace(char_to_remove, "")

def main():
    print("--- Character Remover ---")
    input_string = input("Enter a string: ")
    char_to_remove = input("Enter a character to remove: ")
    result = remove_character(input_string, char_to_remove)
    print(f"Resulting string: {result}")

if __name__ == "__main__":
    main()
