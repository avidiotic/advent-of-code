import re
from collections import defaultdict
from itertools import product
import time


data = open('Puzzle3_input.txt', 'r').read().split('\n')
measurements = (map(int, re.findall(r'-?\d+', line)) for line in data)

cloth_map = defaultdict(list)
cloth_map_2 = defaultdict(list)

start = time.time()
for claim_no, coord_x, coord_y, w, h in measurements:
    
    for i in range(coord_x, coord_x+w):
        for j in range(coord_y, coord_y+h):
            cloth_map[(i,j)].append(claim_no)

print(sum(1 if len(cloth_map[key])>1 else 0 for key in cloth_map))
print(f'Nested loops took {time.time() - start}')

start = time.time()
for claim_no, coord_x, coord_y, w, h in measurements:
    
    for sq in product(range(coord_x, coord_x+w), range(coord_y, coord_y+h)):
        cloth_map_2[sq].append(claim_no)
    
print(sum(1 if len(cloth_map_2[key])>1 else 0 for key in cloth_map_2))
print(f'Product took {time.time() - start}')
