""" 
#3x3
matrix = [
    [4, 8, 1], 
    [9, 7, 2], 
    [5, 6, 0],
]

print(matrix)
print(matrix[0][0])
print(matrix[0][2])
print(matrix[0][1])
"""
#3x3 using loop
matrix = [
    [4, 8, 1], 
    [9, 7, 2], 
    [5, 6, 0],
]
total = 0
for i in range(0,3):
    for j in range(0,3):
        total = total + matrix[i][j]
        #print(matrix[i][j],end=" ")
    #print()
print(total)
