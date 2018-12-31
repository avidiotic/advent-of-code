import re
from collections import defaultdict

input_file = open('Puzzle4_input.txt','r')
data = input_file.read().split('\n')
data.sort()


entry = [(list(map(int,re.findall(r'\d+',line))), re.findall(r'[a-zA-Z].+',line)) for line in data]
log_gt = defaultdict(int)
log_g = defaultdict(int)
log_t = defaultdict(int)

for timecode, text in entry:
    date = str(timecode[1])+"-"+str(timecode[2])
    time_end_index = timecode[4]
    if 'begins shift' in text[0]:
        guard = timecode[5]
        asleep = None
    elif 'falls asleep' in text[0]:
        asleep = timecode[4]
    elif 'wakes up' in text[0]:
        for t in range(asleep, timecode[4]):
            log_gt[(guard,t)] += 1
            log_g[guard] += 1

def max_g(d):
    best = None
    for k,v in d.items():
        if(best is None or v > d[best]):
            best = k
    return(best)



def max_t(d):
    best = None
    for (guard, time) in d:
        if(guard == best_guard):
            if(best is None or d[(guard,time)] > d[best]):
                best = (guard, time)
    return(best[1])

best_guard = max_g(log_g)
best_time = max_t(log_gt)
print(best_guard * best_time)

def max_gt(d):
    best = None
    for (guard,time) in d:
        if(best is None or d[(guard,time)] > d[best]):
            best = (guard,time)
    return(best)
(best_guard, best_time) = max_gt(log_gt)
print(best_guard*best_time)       