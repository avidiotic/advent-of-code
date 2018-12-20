input_file = open('Puzzle1_input.txt','r')
freq = [int(n) for n in input_file.read().split('\n')]
print(sum(freq))
# Solution = 513