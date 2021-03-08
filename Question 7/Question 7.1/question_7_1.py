L1 = 50
L2 = 57

def co2index(x1,x2):
    global L1
    global L2
    index = x1 + L1 * x2
    return index

def index2co(index):
    global L1
    global L2
    x1 = index % L1
    x2 = index // L1
    return x1,x2

coordinates = []
with open('input_coordinates_7_1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = lines[1:]
    for line in lines:
        co = line.strip().split()
        x1, x2 = int(co[0]), int(co[1])
        coordinates.append((x1,x2))

index = []
with open('input_index_7_1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = lines[1:]
    for line in lines:
        index.append(int(line.strip()))

        
with open('output_coordinates_7_1.txt', 'w', encoding='utf-8') as f:
    string = 'x1\tx2\n'
    for index_ in index:
        co = index2co(index_)
        string += '{}\t{}\n'.format(co[0],co[1])
    f.write(string)
    

with open('output_index_7_1.txt', 'w', encoding='utf-8') as f:
    string = 'index\n'
    for co in coordinates:
        index = co2index(co[0],co[1])
        string += '{}\n'.format(index)
    f.write(string)

    