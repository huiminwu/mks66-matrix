"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for i in range(4):
        line = ""
        for row in matrix:  #row should be [x, y, z, 1]
            line = line + str(row[i]) + " "
        print(line)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    pts = len(matrix); #assigns the # of points in the matrix
    for i in range(pts):
        matrix[i][i] = 1

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp = [r[:] for r in m2] #creating temporary copy of m2
    for row in range(len(m1)): #through every row
        for column in range(len(temp[0])): #through every column
            total = 0
            for cell in range(len(m1[0])): #through every column
                total += m1[row][cell] * temp[cell][column]
            m2[row][column] = total


