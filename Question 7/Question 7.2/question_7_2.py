
L = [4, 8 ,5, 9, 6, 7]
def co2index(x):    #x:[x1,..,x6]
    global L
    temp = 1
    index = 0
    for i in range(len(L)):
        index += temp * x[i]
        temp *= L[i]
    return index

def index2co(index):
    global L
    x = []
    temp = index
    for i in range(len(L) - 1):
        x.append(temp % L[i])
        temp = temp // L[i]
    x.append(temp)
    return x    #x:[x1,x2,...,x6] 

coordinates = []
with open('input_coordinates_7_2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = lines[1:]
    for line in lines:
        co = line.strip().split()
        x1, x2, x3, x4, x5, x6 = int(co[0]), \
            int(co[1]), int(co[2]), int(co[3]), int(co[4]), int(co[5])
        coordinates.append((x1,x2,x3,x4,x5,x6))

index = []
with open('input_index_7_2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = lines[1:]
    for line in lines:
        index.append(int(line.strip()))

        
with open('output_coordinates_7_2.txt', 'w', encoding='utf-8') as f:
    string = 'x1\tx2\tx3\tx4\tx5\tx6\n'
    for index_ in index:
        co = index2co(index_)
        string += '{}\t{}\t{}\t{}\t{}\t{}\n'.format(co[0], co[1], co[2], co[3], co[4], co[5])
    f.write(string)
    

with open('output_index_7_2.txt', 'w', encoding='utf-8') as f:
    string = 'index\n'
    for co in coordinates:
        index = co2index(co)
        string += '{}\n'.format(index)
    f.write(string)

    