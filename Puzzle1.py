from collections import defaultdict
from itertools import cycle

# Part 1

data = open('Puzzle1_input.txt', 'r').read().split('\n')
print(sum(int(n) for n in data))

# Solution = 513


# Part 2

summed_frequency = defaultdict(int)
sum = 0

for value in cycle(int(n) for n in data):
	sum += value
	summed_frequency[sum] += 1
	if summed_frequency[sum] == 2:
		print(sum)
		break
		
# Solution = 287
