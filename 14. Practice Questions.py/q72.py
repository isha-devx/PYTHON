"""
Q71
Given a 3x3 matrix, print only the anti diagonal elements and replace everything else with an asterisk(*).

1  2  3
4  5  6
7  8  9

*  *  3
*  5  *
7  *  *
"""


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
r = len(matrix)
c = len(matrix[0])
for i in range(0,r):
    for j in range(0,c):
        if i+j==2:
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ")
    print()


#Q for 4x4 matrix        
"""
Given a 4x4 matrix as input, print its lower triangle.
Replace all elements in the upper triangle (above the main diagonal) with an asterisk (*).

1  2  3  5
4  5  6  1
7  8  9  7
9  7  3  1

*  *  *  4
*  *  7  *
*  10 *  *
13 *  *  *  
"""
matrix = [
    [1, 2, 3, 5],
    [4, 5, 6, 1],
    [7, 8, 9, 7],
    [9, 7, 3, 1],
]
r = len(matrix)
c = len(matrix[0])
for i in range(0,r):
    for j in range(0,c):
        if i+j==r-1:  #or i+j==3
            print(matrix[i][j], end=" ")
        else:
            print("*", end =" ")
    print()

         

