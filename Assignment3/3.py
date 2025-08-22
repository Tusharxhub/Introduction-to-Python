# 3.	Find the second largest number in a list of numbers without sorting the entire list.

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements

    first = second = float('-inf')
    for n in numbers:
        if n > first:
            second = first
            first = n
        elif first > n > second:
            second = n
    return second


my_list = [10, 20, 4, 45, 99]
second_largest = find_second_largest(my_list)
print(f"The second largest number is: {second_largest}")

