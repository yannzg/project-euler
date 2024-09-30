# Path Sum: Two Ways

# Using dynamic programming

import numpy as np

def minimal_sum():
    with open("resources/0081_matrix.txt", 'r') as file:
        lines = file.readlines()

    M = []
    for line in lines:
        row = list(map(int, line.split(',')))
        M.append(row)
    
    M = np.array(M)
    rows, cols = M.shape
    dp = np.zeros_like(M)
    dp[0, 0] = M[0, 0]

    # First row
    for j in range(1, cols):
        dp[0, j] = dp[0, j-1] + M[0, j]
    
    # First column
    for i in range(1, rows):
        dp[i, 0] = dp[i-1, 0] + M[i, 0]

    # Full table
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i, j] = M[i, j] + min(dp[i-1, j], dp[i, j-1])

    min_sum = dp[rows - 1, cols - 1]

    return min_sum


if __name__ == "__main__":
    print(minimal_sum())