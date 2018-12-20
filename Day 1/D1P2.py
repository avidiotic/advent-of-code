input_file = open('Puzzle1_input.txt','r')
frq = [int(n) for n in input_file.read().split('\n')]

total = [0]
repeat = 0
count = 0
len_frq = len(frq)

while (repeat == 0):
    for index, val in enumerate(frq):
        new_total = total[count*len_frq + index] + val
        if new_total in total[0:]:
            repeat = 1
            break
        total.append(new_total)
    count = count + 1

print(count)
print("Result:",new_total)




