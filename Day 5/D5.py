data = open('file.in','r').read().strip()

def reduce_data(text):
    data_old = None
    while data_old != text:
        data_old = text
        for i in range(26):
            text = text.replace(chr(ord('a')+i)+chr(ord('A')+i),'')
            text = text.replace(chr(ord('A')+i)+chr(ord('a')+i),'')
    return(len(text))

print(reduce_data(data))

best = None
for i in range(26):
    data_replaced = data
    data_replaced = data_replaced.replace(chr(ord('a')+i),'')
    data_replaced = data_replaced.replace(chr(ord('A')+i),'')
    val = reduce_data(data_replaced)
    if(best is None or val < best):
        best = val
    
print(best)