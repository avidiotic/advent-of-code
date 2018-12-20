import itertools

input_file = open('Puzzle2_input.txt','r')
ids = input_file.read().split('\n')


def diff_str(s1,s2):
    diff = []
    for x,y in zip(s1,s2):
        diff.append(abs(ord(x)-ord(y)))
    return diff
    
def test_str(s1,s2):    
    diff = diff_str(s1,s2)
    return sum(i > 0 for i in diff)

def compare_str(s1,s2):
    diff = diff_str(s1,s2)
    chars = []
    for i, val in enumerate(diff):
        if (val==0):
            chars.append(s1[i])
    return ''.join(chars)

for a,b in itertools.combinations(ids,2):
    if(test_str(a,b) == 1):
        print(compare_str(a,b))