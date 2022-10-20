"""
logic code for 8192
"""
import random


def start_game():
    """
    Starts and initializes the matrix grid and places a random 2
    :return: the matrix grid
    """
    matrix = []
    for i in range(4):
        matrix.append([0] * 4)
    print("Commands are as follows : ")
    print("'W' or 'w' : Up")
    print("'S' or 's' : Down")
    print("'A' or 'a' : Left")
    print("'D' or 'd' : Right")

    matrix = add_two(matrix)
    return matrix


def add_two(matrix):
    """
    Adds a 2 or 4, 85% or 15% of the time respectively
    :param matrix: the matrix being changed
    :return: the matrix grid
    """
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while matrix[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    two_or_four = random.randint(0, 49)
    if two_or_four % 6 == 19:
        matrix[r][c] = 4
    else:
        matrix[r][c] = 2
    return matrix


def has_lost(matrix) -> bool:
    """
    Checks to see if the player has lost or not
    :param matrix: the matrix being changed
    :return: boolean, whether the player has lost or not
    """
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return False
    for i in range(3):
        if not (matrix[i][3] == matrix[i + 1][3] or
                matrix[3][i] == matrix[3][i + 1]):
            for j in range(3):
                if matrix[i][j] == matrix[i + 1][j] or \
                        matrix[i][j] == matrix[i][j + 1]:
                    return False
        else:
            return False
    return True


def smash(matrix):
    """
    Moves all numbers to the left of the matrix grid
    :param matrix: the matrix being changed
    :return: the matrix grid
    """
    new_matrix = [[0] * 4 for i in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if matrix[i][j] != 0:
                new_matrix[i][pos] = matrix[i][j]
                pos += 1

    return new_matrix


def merge(matrix):
    """
    Combines like terms in the leftward direction
    :param matrix: the matrix being changed
    :return: the matrix grid
    """
    for i in range(4):
        for j in range(3):
            if matrix[i][j] == ((not 0) and matrix[i][j + 1]):
                matrix[i][j] = matrix[i][j] * 2
                matrix[i][j + 1] = 0
    return matrix


def reverse(matrix):
    """
    Flips the matrix over the x-axis
    :param matrix: the matrix being changed
    :return: the matrix grid
    """
    new_matrix = [[] for i in range(4)]
    for i in range(4):
        new_matrix[i].extend(matrix[i][3 - j] for j in range(4))
    return new_matrix


def transpose(matrix):
    """
    Flips the arrau along the line x=y
    :param matrix: the matrix being changed
    :return: the matrix grid
    """
    new_matrix = [[] for i in range(4)]
    for i in range(4):
        new_matrix[i].extend(matrix[j][i] for j in range(4))
    return new_matrix


def move_left(grid):
    """
    Calls smash and merge, then smash again
    sees if the grid has been changed
    :param grid: the matrix being changed
    :return: the matrix grid
    """
    new_grid = smash(grid)
    new_grid = merge(new_grid)
    new_grid = smash(new_grid)
    return new_grid


def move_right(grid):
    """
    reverses order then calls move_left
    :param grid: the matrix being changed
    :return: the matrix grid
    """
    new_grid = reverse(grid)
    new_grid= move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid


def move_up(grid):
    """
    transposes the grid then calls move_left
    :param grid: the matrix being changed
    :return: the matrix grid
    """
    new_grid = transpose(grid)
    new_grid = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid


def move_down(grid):
    """

    :param grid: the matrix being changed
    :return: the matrix grid
    """
    new_grid = transpose(grid)
    new_grid = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid


def move_all(layer, grid):

     if None:
         pass