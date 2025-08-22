# 4. Generate all possible permutations of a given string.
# Prints each unique permutation (handles duplicate characters) in lexicographic order.

from collections import Counter

def permute_unique(s: str) -> None:
	counts = Counter(s)
	path = []
	n = len(s)

	def backtrack():
		if len(path) == n:
			print(''.join(path))
			return
		for ch in sorted(counts.keys()):  # sorted for lexicographic order
			if counts[ch] == 0:
				continue
			counts[ch] -= 1
			path.append(ch)
			backtrack()
			path.pop()
			counts[ch] += 1

	backtrack()

permute_unique(input().strip())

