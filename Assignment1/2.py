# 2.	A high-security vault uses a custom PIN authentication mechanism. To reduce the chances of brute-force attacks, the system only allows PINs that are Neon Numbers.
# The rule is:
# A PIN is valid if the sum of the digits of its square equals the PIN itself.
# Your Task: Write a Python program that reads a numeric PIN input by the user and validates whether it is a Neon Number or not.
# Sample Test Cases

# 	Input	Output
# Test Case 1	9	Neon Number
# Test Case 2	12	Not Neon Number
# Test Case 3	10	Not Neon Number
# Test Case 4	0	Neon Number
# Test Case 5	1	Neon Number
# Test Case 6	2	Not Neon Number






def is_neon_number(pin):
  """
  Checks if a given number is a Neon Number.

  Args:
    pin: An integer representing the user's PIN.

  Returns:
    A string indicating whether the number is a "Neon Number" or "Not Neon Number".
  """
  # Calculate the square of the PIN
  square = pin * pin
  
  # Sum the digits of the square
  sum_of_digits = 0
  # Convert the square to a string to iterate through its digits
  for digit in str(square):
    sum_of_digits += int(digit)
    
  # Check if the sum of digits equals the original PIN
  if sum_of_digits == pin:
    return "Neon Number"
  else:
    return "Not Neon Number"

# Get PIN from the user
try:
  user_pin = int(input("Enter your PIN: "))
  # Validate the PIN and print the result
  result = is_neon_number(user_pin)
  print(result)
except ValueError:
  print("Invalid input. Please enter a numeric PIN.")