#Check if two strings are anagrams of each other (contain the same characters, but possibly in a different order).

def are_anagrams(str1: str, str2: str) -> bool:
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    # Check if sorted characters are the same
    return sorted(str1) == sorted(str2)

def main():
    print("--- Anagram Checker ---")
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    if are_anagrams(string1, string2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

if __name__ == "__main__":
    main()
