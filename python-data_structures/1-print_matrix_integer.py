#!/usr/bin/python3

# creating matric with python 

def print_matrix_integer(matrix=[[]]):
   
   # print a matrix of integers"""" 
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print("{:d}" str.format(matrix[i][j]), end='')
            if j != (len(matrix[i]) -1):
                    print(" ", end="")
