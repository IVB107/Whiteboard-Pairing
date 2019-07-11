class ListNode:
  def __init__(self, value):
      self.value = value
      self.next = None

a = ListNode("Australian Sheperd");
b = ListNode("Beagle");
c = ListNode("Cairne Terrier");
d = ListNode("Dobermann");
e = ListNode("English Mastiff");

a.next = b;
b.next = c;
c.next = d;
d.next = e;

def kth_to_last(head, offset):
  count = 0
  nodes = []
  current = head
  print(f'Starting Node: {count} - {head.value}')
  print(f'Looking for {offset} from last node...')

  while current is not None:
    nodes.append(current)
    count += 1
    current = current.next
  
  print(f'List Length: {count}')
  target = (count - offset)
  if (target >= 0) and (target < len(nodes)):
    return nodes[target].value
  else:
    print(f'Target node {target} is out of range')
    return False

print(f'Returned: {kth_to_last(a, 3)}')
