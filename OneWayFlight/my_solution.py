def reconstructTrip(tickets):
  # This solution is O(2n) --> O(n)
  flights = {}
  route = []
  departure = None
  
  # Add each source: destination pair to dictionary
  for ticket in tickets:
    if ticket[0] is None:
      departure = ticket[1]
    flights[ticket[0]] = ticket[1]
  
  # Add each destination to list until none exists
  while flights[departure] is not None:
    route.append(flights[departure])
    departure = flights[departure]

  print(f'Route: {route}')

tix = [
  ['PIT', 'ORD'],
  ['XNA', 'CID'],
  ['SFO', 'BHM'],
  ['FLG', 'XNA'],
  [None, 'LAX'], 
  ['LAX', 'SFO'],
  ['CID', 'SLC'],
  ['ORD', None],
  ['SLC', 'PIT'],
  ['BHM', 'FLG'],
]

reconstructTrip(tix)