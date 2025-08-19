# 1.	Gautam Gambhir, freshly appointed head coach for India’s 2025 away Test series against England, has asked the new analyst, Aryan, to keep a quirky statistic:
# “At the end of each day’s play,” Gambhir says, “tell me the total runs we scored in every odd-numbered over—1st, 3rd, 5th … all the way up to the last over bowled that day. It helps me spot momentum in the sessions where bowlers are freshest.”
# Aryan realises the job boils down to simple maths: if n is the last over of the day (always a positive integer), he just needs the sum of all odd integers from 1 through n.
# Your task is to step into Aryan’s shoes and automate this little ritual.
# Input Format:
# A single integer
# Output Format:
# A single integer: the sum of all odd numbers from 1 to n
# Sample Test Cases

# 	Input	Output
# Test Case 1	15	64
# Test Case 2	100	2500
# Test Case 3	9	25
# Test Case 4	1	1
# Test Case 5	2	1
# Test Case 6	10	25




def sum_odd_numbers(n):
  """
  Calculates the sum of all odd numbers from 1 to n.

  Args:
    n: An integer representing the last over of the day.

  Returns:
    The sum of all odd numbers from 1 to n.
  """
  if n % 2 == 1:
    # If n is odd
    num_odd = (n + 1) // 2
  else:
    # If n is even
    num_odd = n // 2
  return num_odd * num_odd

# Example Usage:
last_over = 15
total_runs_in_odd_overs = sum_odd_numbers(last_over)
print(f"For a day with {last_over} overs, the sum of runs in odd-numbered overs is: {total_runs_in_odd_overs}")

last_over = 100
total_runs_in_odd_overs = sum_odd_numbers(last_over)
print(f"For a day with {last_over} overs, the sum of runs in odd-numbered overs is: {total_runs_in_odd_overs}")