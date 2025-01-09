# Linked Lists

## Introduction
A linked list is a data structure that optimizes access to the first (head) and last (tail) pieces of data. It is able to read, remove, or change the head and tail in O(1).

## Linked List Structure and Behavior
A linked list is similar to a treasure hunt. You start out with the first clue which then leads you to the next clue and so on until you reach the end. A linked list behaves similarly. The "clue" in a linked list is called a node. The node contains three things: the data being held, directions to the previous node, and directions to the next node. The linked list simply keeps track of the first and last nodes of the list and trusts that it can follow the trail of "clues" to reach any other node. The linked list data structure also keeps track of its size. This is important so as to prevent the need to go counting all the nodes every time the size is needed.

The behavior of the linked list is simple, it is optimized for accessing either end, but supports changes to its more inner nodes as well. To make changes to the center nodes, the linked list iterates accross the nodes until the desired node is reached, then performs the desired operation.

## Linked List Implementation
Below is an implementation of a linked list in python. Carefully read the comments to understand a linked list.

Note: This implementation is for instruction purposes only. Python provides a deque which should be used instead.

```python
class LinkedList:
  """ Linked List - implements key operations of the linked list data structure

  Methods
  -------
  insert_head(value)
    insert a new node at the head of the linked list
  insert_tail(value)
    insert a new node at the tail of the linked list
  insert(index, value)
    insert a new node at the specified index of the linked list
  remove_head()
    remove the head node of the linked list
  remove_tail()
    remove the tail node of the linked list
  remove(index)
    remove the node at the specified index of the linked list
  size()
    return the number of nodes in the linked list
  empty()
    return True if the linked list is empty, otherwise False

  Attributes
  -------
  head : Node
    the first node in the linked list
  tail : Node
    the last node in the linked list
  size : int
    the number of nodes in the linked list
  """

  # The node is a key component of the linked list
  class Node:
    """ Node - implements the node of the linked list data structure

    Methods
    -------
    For simplicity, all attributes are accessed/mutated directly

    Attributes
    -------
    value : any
      the value of the node
    next : Node
      the next adjacent node
    prev : Node
      the previous adjacent node
    """
    def __init__(self, value):
      # A node has three attributes: value, next, and prev

      # The value of the node is the data being stored
      self.value = value
      # The next attribute points to the next node in the linked list
      self.next = None
      # The prev attribute points to the previous node in the linked list
      self.prev = None
      # Note that the next and prev attributes are None when there
      # is no next or previous node, respectively

  def __init__(self):
    # A linked list has three key attributes: head, tail, and size
    
    # The head attribute points to the first node in the linked list
    self.head = None
    # The tail attribute points to the last node in the linked list
    self.tail = None
    # These attributes are important to quickly access either
    # end of the linked list

    # The size attribute keeps track of the number of nodes in the linked list
    self.size = 0
    # This is important so that it does not need to count the number
    # of nodes every time it needs to know the size
  
  def insert_head(self, value):
    """ insert_head - insert a new node at the head of the linked list

    Parameters
    ----------
    value : any
      the value of the new node
    """
    # When inserting a value into the list, a node is created
    new_node = self.Node(value)

    # There is a special case of an empty linked list
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    
    # Otherwise, the new node is inserted at the head as follows
    else:
      # The new node is configured to point to the previous head
      new_node.next = self.head
      # And the previous head is configured to point back to the new node
      self.head.prev = new_node
      # Finally, the linked list is updated to point to the new head
      self.head = new_node
    
    # Finally, the size is updated to reflect the new node
    self.size += 1

  def insert_tail(self, value):
    # This method is similar to insert_head, but the new node is inserted
    # at the tail of the linked list instead

    # The implementation is left out for brevity
    pass

  def insert(self, index, value):
    """ insert - insert a new node at the specified index of the linked list

    Parameters
    ----------
    index : int
      the index of the new node
    value : any
      the value of the new node
    """
    # This method also inserts a new node, but at a specified index
    # of the linked list

    # There are two special cases, inserting at the head or tail by index
    # These are edge cases that need to be handled separately
    # A check is made for these cases and the appropriate method is called
    if index == 0:
      self.insert_head(value)
    elif index == self.size:
      self.insert_tail(value)
    
    # Otherwise, the new node is inserted at the specified index as follows
    else:
      new_node = self.Node(value)
      # This variable tracks the current node being visited
      # It starts at the head of the linked list since only the head
      # and tail are known.
      current = self.head
      # The linked list is traversed until the specified index is reached
      for _ in range(index):
        # This visits the next node in the linked list
        current = current.next

      # At this point, current holds the node at the specified index
      # The new node is inserted before the current node making it the
      # new node at the specified index. That is, current is pushed
      # forward to the next index.

      # The new node is configured to point to the appropriate nodes
      new_node.prev = current.prev
      new_node.next = current

      # The adjacent nodes are updated to point to the new node
      current.prev.next = new_node
      current.prev = new_node

      # The size is always increased when an insertion occurs
      self.size += 1
  

  def remove_head(self):
    """ remove_head - remove the head node of the linked list

    Returns
    -------
    any
      the value of the removed node
    """
    # To prevent errors, a check is made for an empty linked list
    if self.head is None:
      return None
    
    # The value of the head node is stored for later return
    value = self.head.value

    # The head is updated to the next node in the linked list
    self.head = self.head.next
    # If there was another node in the linked list to take the place
    # of the head, it is configured to no longer point to the old head
    if self.head is not None:
      self.head.prev = None
    # Otherwise, if the linked list is now empty, the tail was also
    # the head and is set to None
    else:
      self.tail = None

    # The size is now decreased to reflect the removal of a node
    # Note, this must be done before returning the value
    self.size -= 1

    # The value of the removed node is returned for use by the caller
    return value
  
  def remove_tail(self):
    # This method is similar to remove_head, but the tail node is removed

    # The implementation is left out for brevity
    pass

  def remove(self, index):
    """ remove - remove the node at the specified index of the linked list

    Parameters
    ----------
    index : int
      the index of the node to remove

    Returns
    -------
    any
      the value of the removed node
    """
    # Similar to insert, this method removes a node at a specified index
    # and must also check for the edge cases of the head and tail
    if index == 0:
      return self.remove_head()
    elif index == self.size - 1:
      return self.remove_tail()
    # Otherwise, the linked list is traversed to the specified index
    else:
      # This process is identical to the one we saw in insert
      current = self.head
      for _ in range(index):
        current = current.next

      # Here is where things get different
      # The previous and next nodes are configured to point to each other
      current.prev.next = current.next
      current.next.prev = current.prev
      # The size is updated
      self.size -= 1
      # And the value of the removed node is returned
      return current.value
    
  # The size() and empty() methods are simple and do not require explanation
  # They are excluded for brevity
```

## Stack Syntax

| Function      | Description                                                                | Python Syntax                   |
| ---           | ---                                                                        | ---                             |
| insert_head(value)   | Inserts a value at the front (head) of the list                     | deque_list.appendleft(value)    |
| insert_tail(value)   | Inserts a value at the end (tail) of the list                       | deque_list.append(value)        |
| insert(index, value) | Inserts a value at the specified index                              | deque_list.insert(index, value) |
| remove_head()        | Removes and returns the value at the head of the list               | value = deque_list.popleft()    |
| remove_tail()        | Removes and returns the value at the tail of the list               | value = deque_list.pop()        |
| remove(index)        | Removes the value at the specified index                            | del deque_list[index]           |
| size()               | Returns the number of elements in the linked list                   | len(deque_list)                 |
| empty()              | Returns **True** if the list is empty. Otherwise, returns **False** | len(deque_list) == 0            |

## Common Use Cases

Linked lists are useful when the size of the list is constantly changing. It does not require the client to know the size of the list before memory allocation as memory is only allocated as it is needed. A real world example of a linked list is an operating system's file system. One implementation is to have each directory entry be linked to the next entry within the same directory. This provides a dynamically sized memory for the folder entries.

## Example Problem

Here is a simple example of using a linked list to test if a given string is a palindrome.

Example:
* "racecar" -> True
* "hello" -> False
* "Hannah" -> True


```python
from collections import deque

def is_palindrome(text):
  # Create a linked list from the input text
  linked_list = deque()
  for char in text.lower():
    # Add each character to tail of the linked list
    linked_list.append(char)
  # Note, it would also be valid to use 'linked_list = deque(list(text.lower()))'

  # Compare the head and tail until the linked list is empty or only has one value left
  while len(linked_list) > 1:
    if linked_list.popleft() != linked_list.pop():
      # If the head and tail do not match, the text is not a palindrome
      return False
  
  # If the loop completes without returning False, the text is a palindrome
  return True
```

Click [here](./solutions/linked-list-example.py) to open a runnable python file.

## Tackle This

Implement a function which rotates the values of a linked list by some number. For example, if given the linked list represented by [1, 2, 3, 4, 5] and a rotation amount of 3, the linked list will be rotated by 3 positions and now be represented by [3, 4, 5, 1, 2]. Negative values should also be supported and be interpreted as a rotation in the opposite direction.

You may use the python deque as the linked list implementation.

[Click here](./solutions/linked-list-problem.py) to see the solution.

[Return to Homepage](0-welcome.md)
