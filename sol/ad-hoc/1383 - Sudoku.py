# 1383 - Sudoku
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1383

import itertools


def cols(matrix):
    """generates the matrix's columns"""
    width = len(matrix[0])
    for j in range(width):
        yield [row[j] for row in matrix]


def sections(matrix):
    """generates the matrix's 9x9 sections"""
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            yield (matrix[i][j:j+3] 
                    + matrix[i+1][j:j+3] 
                    + matrix[i+2][j:j+3])


def is_complete(items):
    return set(items) == {1, 2, 3, 4, 5, 6, 7, 8, 9}


def is_solved(matrix):
    '''checks if all the lines, columns and sections have 1..9 numbers'''
    iters = itertools.chain(matrix, cols(matrix), sections(matrix))
    return all(is_complete(x) for x in iters)


def main():
    n = int(input())

    matrix = [0] * 9
    for t in range(1, n + 1):
        for i in range(9):
            matrix[i] = list(map(int, input().split()))

        print('Instancia {}\n{}\n'.format(t, 
            'SIM' if is_solved(matrix) else 'NAO'))


if __name__ == '__main__':
    main()
