"""1. Напишите функцию для транспонирования матрицы"""

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def print_matrix(matrix, n, m):
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()

n, m = int(input()), int(input())
matr = [[i for i in range(n)] for j in range(m)]
print('Исходная матрица: ')
print_matrix(matr, n, m)
print('Транспонированная матрица: ')
print_matrix(transpose_matrix(matr), m, n)
