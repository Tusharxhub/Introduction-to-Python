# 4.	In the land of Codeville, young programmers discover an ancient scroll containing a list of mysterious words — each one part of a secret prefix code used by the town’s old network of messengers. Legend says that hidden among these words is one with special power: the longest word in the list. But there’s a twist — if more than one word shares the longest length, the scroll reveals only the one that appears last in the list.The town’s Code Scribe, Pixel, needs your help. She wants you to write a program that will search through this list and identify the special word according to the rules.
# Write a program that:
# Accepts a single line of input containing a comma-separated list of words from the ancient prefix code.
# Finds and prints:   (a) The longest word in the list.   (b) If multiple words share the maximum length, print the one that appears right-most in the list.
# Sample Test Cases

# 	Input	Output
# Test Case 1	this,sentence,is,quite,long	sentence
# Test Case 2	this,is,a,good,word	word
# Test Case 3	a,ab,abc,abcd,abcde	abcde



# longest_word.py

# Take input (comma-separated words)
words = input("Enter words separated by commas: ").split(",")

# Track the longest word, preferring the rightmost if lengths are equal
longest = ""
for w in words:
    if len(w) >= len(longest):   # >= ensures rightmost wins in a tie
        longest = w

print(longest)
