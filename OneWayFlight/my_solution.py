def reconstructTrip(tickets):
  flights = {}
  route = []
  departure = None
  for ticket in tickets:
    if ticket[0] is None:
      departure = ticket[1]
    flights[ticket[0]] = ticket[1]
  
  while flights[departure] is not None:
    route.append(flights[departure])
    departure = flights[departure]

  # print(f'Flights: {flights}')
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