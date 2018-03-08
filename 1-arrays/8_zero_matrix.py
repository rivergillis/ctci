# Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and columns are set to 0.

# O(n)
def zero_row(matrix, row, n):
    for col_idx in range(n):
        matrix[row][col_idx] = 0

# O(m)
def zero_col(matrix, col, m):
    for row_idx in range(m):
        matrix[row_idx][col] = 0

# O(3mn) = O(mn)
def zero_matrix(matrix):
    if not matrix:
        return

    zeroed_rows = set()
    zeroed_cols = set()

    m = len(matrix) # num rows, length of a col
    n = len(matrix[0]) # num cols, length of a row

    # O(mn)
    for row_idx in range(m):
        for col_idx in range(n):
            if matrix[row_idx][col_idx] == 0:
                zeroed_rows.add(row_idx)
                zeroed_cols.add(col_idx)

    # O(mn)
    for row in zeroed_rows:
        zero_row(matrix, row, n)

    # O(mn)
    for col in zeroed_cols:
        zero_col(matrix, col, m)

if __name__ == '__main__':
    m1 =    [[1, 2, 3, 0],
             [4, 0, 6, 11],
             [7, 8, 9, 12]]
    zero_matrix(m1)
    print(m1)