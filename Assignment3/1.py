# 1.	Given an array of integers from 1 to 100 with one number missing, find the missing number.


def find_missing_number_sum(arr):
  """
  Finds the missing number in a list of unique integers from 1 to 100
  using the summation method.
  """
  n = 100
  # Calculate the expected sum of numbers from 1 to 100
  expected_sum = n * (n + 1) // 2  # Use // for integer division

  # Calculate the actual sum of the numbers in the list
  actual_sum = sum(arr)

  # The difference is the missing number
  return expected_sum - actual_sum

# --- Example Usage ---
# Create a list from 1 to 100
my_list = list(range(1, 101))

# Remove a number to create the test case (e.g., 73)
my_list.remove(73)

# Find the missing number
missing_num = find_missing_number_sum(my_list)
print(f"The list is missing the number: {missing_num}")
# Expected Output: The list is missing the number: 73