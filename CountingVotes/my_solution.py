def countVotes(votes):

  counts = {}
  frontrunner = ''
  highest = 0

  for name in votes:
    if name in counts:
      counts[name] += 1
    elif name not in counts:
      counts[name] = 1
    if counts[name] > highest:
      highest = counts[name]
      frontrunner = name
    if counts[name] == highest:
      if name > frontrunner:
        frontrunner = name
  return frontrunner


print(countVotes(['veronica', 'mary', 'alex', 'james', 'mary', 'michael', 'alex', 'michael']))

  # - iterate through the array of names
  # - for each name, check if it is in the dictionary
  #   - if name not in dictionary, add name as key with value == 1
  #   - if name in dictionary, value += 1
  # - compare key value with highest
  #   - if value > highest, update highest
  #     - update frontrunner
  #   - if value == highest
  #     - compare name with frontrunner
  #       - if name > frontrunner, frontrunner = name

  
