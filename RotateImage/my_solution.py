def rotateImage(matrix):
  matrix = matrix
  newArr = []

  for i in range(len(matrix)-1, -1, -1):
    print(matrix[i])
    row = []
    for j in range(len(matrix)):
      row.append(matrix[j][i])
    newArr.append(row)
  
  print(f'New Array: {newArr}')
  return newArr


rotateImage([
  [1, 2],
  [3, 4]
]);