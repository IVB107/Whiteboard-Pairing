def matrix_spiral(inputMatrix):


output = []

row = 5
column = 4
count = 0
steps = 0

top = len(inputMatrix[0])
right = len(inputMatrix) - 1
bottom = top - 1

# for i in inputMatrix:
#   count += len(inputMatrix[i])

count = len(inputMatrix)*len(inputMatrix[0])

while steps < count:



while steps is less than count:
  start at [0, 0]
  for each element in row:
    append element to ouput array
  subtract row length by 1

  for each element in column:
    append element to output array
  subtract column by 1

  for each element in row (counting down):
    append element to ouput array
  subtract row length by 1

  for each element in column (counting down):
    append element to output array
  subtract column by 1
