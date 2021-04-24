def find_row_column_max_element(matrix):
    """
    Example:
    3 1 2
    1 3 4
    3 3 3

    return: 1,2
    """
    row = 0
    column = 0
    max = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[i][j] > max:
                max = matrix[i][j]
                row = i
                column = j
    return row, column
