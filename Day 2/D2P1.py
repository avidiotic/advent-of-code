input_file = open('Puzzle2_input.txt','r')
ids = input_file.read().split('\n')
twos = [0]*len(ids)
threes = [0]*len(ids)

def get_reps(word, n):
    reps = 0
    for item in word:
        if (word.count(item) == n):
            reps = 1
    return reps

twos = map(lambda x: get_reps(x,2), ids)
threes = map(lambda x: get_reps(x, 3), ids)

print(sum(twos)*sum(threes))
