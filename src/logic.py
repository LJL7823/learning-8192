"""
logic code for 2048
"""
import random


def start_game():
    matrix = []
    for i in range(4):
        matrix.append([0] * 4)
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    matrix = add_two(matrix)
    return matrix


def add_two(matrix):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while matrix[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    two_or_four = random.randint(0, 19)
    if two_or_four % 6 == 0:
        matrix[r][c] = 4
    else:
        matrix[r][c] = 2
    return matrix


def has_lost(matrix) -> bool:
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return False
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == matrix[i + 1][j] or \
                    matrix[i][j] == matrix[i][j + 1]:
                return False
    for i in range(3):
        if matrix[j][3] == matrix[j + 1][3]:
            return False
    for i in range(3):
        if matrix[3][i] == matrix[3][i + 1]:
            return False

    return True


def smash(matrix):
    changed = False
    new_matrix = []
    for i in range(4):
        new_matrix.append([0] * 4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if matrix[i][j] != 0:
                new_matrix[i][pos] = matrix[i][j]
                if j != pos:
                    changed = True
                pos += 1

    return new_matrix, changed


def merge(matrix):
    changed = False

    for i in range(4):
        for j in range(3):
            if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0:
                matrix[i][j] = matrix[i][j] * 2
                matrix[i][j + 1] = 0
                changed = True
    return matrix, changed


def reverse(matrix):
    new_matrix = []
    for i in range(4):
        new_matrix.append([])
        for j in range(4):
            new_matrix[i].append(matrix[i][3 - j])
    return new_matrix


def transpose(matrix):
    new_matrix = []
    for i in range(4):
        new_matrix.append([])
        for j in range(4):
            new_matrix[i].append(matrix[j][i])
    return new_matrix


def move_left(grid):
    new_grid, changed1 = smash(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed2 or changed1
    new_grid, temp = smash(new_grid)
    return new_grid, changed


def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed


def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed


def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed
