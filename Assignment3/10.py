# Find the common elements between two lists.



def find_common_elements(list1: list, list2: list) -> list:
    return [element for element in list1 if element in list2]

def main():
    print("--- Common Elements Finder ---")
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    common_elements = find_common_elements(list_a, list_b)
    print(f"Common elements: {common_elements}")

if __name__ == "__main__":
    main()
