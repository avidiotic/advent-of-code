import re
from collections import defaultdict

input_file = open('Puzzle3_input.txt','r')
data = input_file.read().split('\n')

claims = [list(map(int,re.findall(r'-?\d+',line))) for line in data]
map_cloth = defaultdict(list)
overlap = defaultdict(list)

for claim_no, start_x, start_y, w, h in claims:
    overlap[claim_no] = set()
    for i in range(start_x, start_x+w):
        for j in range(start_y, start_y+h):
            if map_cloth[(i,j)]:
                for existing_claim in map_cloth[(i,j)]:
                    overlap[existing_claim].add(claim_no)
                    overlap[claim_no].add(existing_claim)
            map_cloth[(i,j)].append(claim_no)
    
count_twooverlaps = [sq for sq in map_cloth if len(map_cloth[sq])>1]
print(len(count_twooverlaps)) #part 1

no_overlaps = [claim for claim in overlap if len(overlap[claim]) == 0]
print(no_overlaps)


