from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
my_matrix = [[1,2,3,1],[4,5,6,1],[7,8,9,1]]
one_matrix = [[4, 5, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print_matrix(my_matrix)
print_matrix(one_matrix)
ident(matrix)
#print_matrix(matrix)
matrix_mult(matrix, one_matrix)
print_matrix(one_matrix)

draw_lines( matrix, screen, color )
display(screen)
