import re
from collections import defaultdict
from itertools import product

data = open('Puzzle3_input.txt', 'r').read().split('\n')
measurements = (map(int, re.findall(r'-?\d+', line)) for line in data)

cloth_map = defaultdict(list)
overlap = defaultdict(list)

for claim_no, coord_x, coord_y, w, h in measurements:
    overlap[claim_no] = set()
    for sq in product(range(coord_x, coord_x+w), range(coord_y, coord_y+h)):
        if cloth_map[sq]:
            for existing_claim in cloth_map[sq]:
                overlap[claim_no].add(existing_claim)
                overlap[existing_claim].add(claim_no)
        cloth_map[sq].append(claim_no)


print(sum(1 if len(cloth_map[key]) > 1 else 0 for key in cloth_map))
# Solution of Part 1 = 121259

print([key for key in overlap if len(overlap[key]) == 0][0])
# Solution of Part 2 = 239
