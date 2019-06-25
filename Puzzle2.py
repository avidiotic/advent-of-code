from collections import Counter
from itertools import combinations


# Part 1

data = open('Puzzle2_input.txt', 'r').read().split('\n')
stats = [0, 0]

for item in data:
	count = Counter(item).values()
	if 2 in count:
		stats[0] += 1
	if 3 in count:
		stats[1] += 1

print(stats[0]*stats[1])

# Solution = 8296


# Part 2

def common_char(str1, str2):
	return ''.join((char1 if char1 == char2 else '' for char1, char2 in zip(str1, str2))) 

for str1, str2 in combinations(data, 2):
	diff = sum(1 if ord(char1) - ord(char2) != 0 else 0 for char1, char2 in zip(str1, str2))
	if diff == 1:
		print(common_char(str1, str2))
		
# Solution = pazvmqbftrbeosiecxlghkwud		
