matrix1 = []
with open('input_question_4', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        temp = line.strip().split()
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        matrix1.append(temp)
#print(matrix1)
matrix2 = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
#print(matrix2)

class_num = 1
def connect(matrix, i, j):
    m = len(matrix)
    n = len(matrix[0])
    global matrix2
    global class_num
    flag = False
    if matrix[i][j] == 1:
        if matrix2[i][j] != 0:
            return False
        else:
            flag = True
        matrix2[i][j] = class_num
        if i > 0 and matrix[i-1][j] == 1 and matrix2[i-1][j] == 0:
            connect(matrix, i-1, j)
        if j > 0 and matrix[i][j-1] == 1 and matrix2[i][j-1] == 0:
            connect(matrix, i, j-1)
        if i < m-1 and matrix[i+1][j] == 1 and matrix2[i+1][j] == 0:
            connect(matrix, i+1, j)
        if j < n-1 and matrix[i][j+1] == 1 and matrix2[i][j+1] == 0:
            connect(matrix, i, j+1)
            
    return flag
        
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        if matrix2[i][j] == 0:
            if connect(matrix1, i, j):
                class_num += 1

with open('output_question4', 'w', encoding = 'utf-8') as f:
    string = ''
    for i in range(len(matrix2)):
        for j in range(len(matrix2[0])):
            string += str(matrix2[i][j]) + '\t'
        string += '\n'
    f.write(string)