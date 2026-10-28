#Q73
#iven a matrix 4x4, print only the border elements and replace the inner elements with an asterisk(*).
"""
INPut
1  2  3  4
5  6  7  8
9  10 11 12    
13 14 15 16
OUTPUT
1  2  3  4
5  *  *  8
9  *  * 12
13 14 15 16
"""

matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],   
    [13, 14, 15, 16],
]
r = len(matrix)
c = len(matrix[0])
for i in range(0,r):
    for j in range(0,c):
        if (i==1 or i==2) and (j==1 or j==2):
            print("*",end=" ")
        else:
            print(matrix[i][j],end=" ")
    print()