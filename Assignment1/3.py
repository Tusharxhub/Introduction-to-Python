# 3.	While analysing intercepted communications, TASC officer Srikant Tiwari suspects that some messages might be carrying hidden signals. One of the red flags used by the agency is the density of vowels in a message — unusually high vowel counts may indicate a coded alert.
# To assist in screening these messages quickly, a script is needed to count the number of vowels in any given string.
# Write a Python program that:
# Takes a message as input.
# Counts the number of vowels (a, e, i, o, u — both uppercase and lowercase).
# Prints the vowel count.
# Input Format:
# A single line containing a string .
# Output Format:
# A single integer — the count of vowels (A, E, I, O, U in both uppercase and lowercase).
# Sample Test Cases

# 	Input	Output
# Test Case 1	Data Science	5
# Test Case 2	qwrtypsdfghj	0
# Test Case 3	I love programming!	6
# Test Case 4	hello	2
# Test Case 5	PYTHON	1
# Test Case 6	OpenAI 123	4



def count_vowels(message):
  """
  Counts the number of vowels in a given string.

  Args:
    message: A string which may contain a hidden signal.

  Returns:
    An integer representing the total count of vowels.
  """
  # A set of all vowels for quick lookup (both lowercase and uppercase)
  vowels = "aeiouAEIOU"
  vowel_count = 0
  
  # Iterate through each character in the message
  for char in message:
    # Check if the character is a vowel
    if char in vowels:
      vowel_count += 1
      
  return vowel_count

# Get the message from the user
try:
  input_message = input("Enter the message to analyze: ")
  # Calculate and print the vowel count
  result = count_vowels(input_message)
  print(f"Vowel count: {result}")
except Exception as e:
  print(f"An error occurred: {e}")