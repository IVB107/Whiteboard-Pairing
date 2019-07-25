# def time_planner(person_A, person_B, duration):

  # ----- First Pass Solution -----
  # Time Complexity: O(n + n^2)

  # Remove time slots that are less than meeting duration
  # person_A = [i for i in person_A if i[1]-i[0] >= duration]
  # person_B = [i for i in person_B if i[1]-i[0] >= duration]

  # # Return empty array if one or both schedules are empty
  # if len(person_A) < 1 or len(person_B) < 1:
  #   return []

  # match = []

  # for slot_a in person_A:
  #   for slot_b in person_B:
  #     if slot_b[0] >= slot_a[0] and slot_b[0] <= slot_a[1]:
  #       match = [slot_b[0], slot_b[0] + duration]
  #       return print(f'Match: {match}')
  
  # # Return empty array
  # return print(f'Match: {match}')
  

# ----- My version of model solution -----
# Time Complexity: O(n + n) --> O(2n) --> O(n)

def time_planner(person_A, person_B, duration):
  a = 0
  b = 0

  while a < len(person_A) and b < len(person_B):
    start = max(person_A[a][0], person_B[b][0])
    end = min(person_A[a][1], person_B[b][1])

    if start + duration <= end:
      return print([start, start + duration])
    
    if person_A[a][1] < person_B[b][1]:
      a += 1
    else:
      b +=1

  return print([])


time_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8)
time_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 72]], 12)
time_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12)