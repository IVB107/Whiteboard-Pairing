
class ListNode:
  def __init__(self, value):
      self.value = value
      self.next = None


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(2)
e = ListNode(1)

print(a.value, b.value, c.value, d.value, e.value) 

def recursively_link(link_string, node=None, origin=None):
    first_letter = link_string[0:1]
    new_node = ListNode(value=first_letter)

    if node is None:
        origin = new_node
    else:
        node.next = new_node

    string_remainder=link_string[1:]
    if string_remainder:
        return recursively_link(string_remainder, new_node, origin)
    else:
        return origin

new_list = recursively_link('123454321')

print(new_list)


def palindrome(head_node):
  my_list = []
  current = head_node

  while current is not None:
    print(f'Current: {current.value}')
    my_list.append(current.value)
    current = current.next
    
  print(f'List: {my_list}')

  flipped = [char for char in my_list]
  flipped.reverse()
  # my_list[0:].reverse()

  print(f'Flipped: {flipped}')
  if my_list == flipped:
    print('Valid Palindrome')
    return True
  else:
    print('Not a palindrome')
    return False

palindrome(new_list)