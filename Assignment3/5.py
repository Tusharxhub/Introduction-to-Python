# Merge two sorted lists into a single sorted list.


def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
        
    return merged_list

def main():
    print("--- Merge Two Sorted Lists ---")

    list_a = [1, 3, 5, 7, 9]
    list_b = [2, 4, 6, 8, 10]
    
    print(f"List 1: {list_a}")
    print(f"List 2: {list_b}")

    merged = merge_sorted_lists(list_a, list_b)

    print(f"\nMerged sorted list: {merged}")

if __name__ == "__main__":
    main()