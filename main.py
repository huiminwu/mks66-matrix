from display import *
from draw import *
from matrix import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14], [15,16,17,18], [19,20,21,22], [23,24,25,26]]
matrix_mult(A, B)
print_matrix(A)
print_matrix(B)
matrix_mult(B, A)
print_matrix(A)
print_matrix(B)
ident(matrix)
matrix_mult(matrix, A)
print_matrix(A)

drawingL = new_matrix()
drawingR = new_matrix()
i = 0
while(i < 500):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    #add_edge(drawing, x, y, 0, y, x, 0)
    if (y > x):
        add_edge(drawingR, y, x, 0, x, x, 0)
    else:
        add_edge(drawingL, y, x, 0, x, x, 0)
    i = i + 1
draw_lines(drawingR, screen, [255,193,181])
draw_lines(drawingL, screen, [181,229,255])
display(screen)
