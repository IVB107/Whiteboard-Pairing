
def zeros(list):
  #  initialize pointer a to beginning of list
  a = 0
  #  initialize pointer b to end of list
  b = len(list) - 1
  while b >= a:
    if list[a] == 0 and list[b] != 0:
      list[a], list[b] = list[b], list[a]
    if list[b] == 0:
      b -= 1
    if list[a] != 0:
      a += 1

  return a

print(zeros([0, 0, 0, 0, 0]))