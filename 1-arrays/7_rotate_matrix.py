# Given an image represented by an NxN matrix, where each pixel is
# 4 bytes, write a method to rotate the iamge by 90 degrees.
# Can you do this in place?

# rotate 90 clockwise

# O(n^2)
def rotate(matrix):
    # Alternative: return zip(*matrix[::-1])
    rotated_matrix = []
    n = len(matrix)

    for row_index in range(n):
        rotated_row = []
        for col_index in range(n):
            rotated_row.append(matrix[col_index][n-1-row_index])
        rotated_matrix.append(rotated_row)

    return rotated_matrix

# Unfinished.
def rotate_in_place(matrix):
    def swp(idx1, idx2):
        matrix[idx1[0]][idx1[1]], matrix[idx2[0]][idx2[1]] = \
            matrix[idx2[0]][idx2[1]], matrix[idx1[0]][idx1[1]]
    swp((0, 0), (0, 1))

if __name__ == '__main__':
    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print(rotate(m))

    m2 = [[1, 2],
          [3, 4]]
    rotate_in_place(m2)
    print(m2)

    # Rotated m 90 degrees counterclockwise should be
    # m =   [[3, 6, 9],
    #        [2, 5, 8],
    #        [1, 4, 7]]
    # [[m[0][2], m[1][2], m[2][2]],
    #  [m[0][1], m[1][1], m[2][1]], ...