def rotate(matrix):
  """
    - reverse rows -> .reverse()
    - flip it diagonally

    For example:
    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

    Reverse:
    
    [[7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]].
    
    Flip diagonally
    [[7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]]
  """
  matrix.reverse()
  for i in range(len(matrix)):
      for j in range(i):
          matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Time: O(n*m)
# Space: O(1)