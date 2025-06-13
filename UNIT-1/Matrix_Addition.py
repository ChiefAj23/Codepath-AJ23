# Problem 1: Matrix Addition
# Write a function add_matrices() that accepts to n x m matrices matrix1 and matrix2.
# The function should return an n x m matrix sum_matrix that is the sum of the given
# matrices such that each value in sum_matrix is the sum of values of corresponding elements in matrix1 and matrix2.

# def add_matrices(matrix1, matrix2):
#     pass
# Example Usage

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# add_matrices(matrix1, matrix2)
# Example Output:

# [
#     [10, 10, 10],
#     [10, 10, 10],
#     [10, 10, 10]
# ]
##################################################################################################################
#Solution:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

def add_matrices(matrix1, matrix2):

    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")

    sum_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # Iterate through each element and compute the sum
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            sum_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return sum_matrix

print(add_matrices(matrix1, matrix2))
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)