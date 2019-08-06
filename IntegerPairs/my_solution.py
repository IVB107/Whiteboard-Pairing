def int_pair(arr, int):

  pairs = []

  for i in range(0, len(arr) - 2):
    for j in range(i+1, len(arr)):
      # if i != j:
        if arr[i] + arr[j] == int:
          pair = f'{arr[i]} {arr[j]}'
          # if pair not in pairs:
          pairs.append(pair)

  print(f'PAIRS: {pairs}')
  return

int_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)


#  for each integer i in the list
  #  inner loop: for each int j
    #  if i != j:
      #  check sum of i + j
      #  if sum of i + j == int:
        #  append string pair to pairs list []