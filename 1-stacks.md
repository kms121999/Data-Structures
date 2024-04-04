# Stacks

## Introduction
A stack is a data structure that optimizes for "Last In, First Out" functionality. This means that it is very quick at adding an element as well as returning the most recent element added.

## How Stacks Behave
An appropriate example of the behavior of a stack is a real world stack of plates. When you unload the dishwasher, you put each clean plate on the top of the stack of dishes in the cabinet. Later, when it's time to eat, you take the top plate off to use. Every meal, you take the next. Eventually, you wash dishes again and return dishes to the top of the stack. The data structure behaves just like this. There are two vital operations that distinguish a stack: push and pop. Push adds an element to the top of the stack, and pop removes the top element from the stack. Stacks also support methods to test if the stack is empty and to get the number of elements in the stack.

## Stack Implementation
The key idea of a stack is to optimize placing and removing from the "top" of the stack. Since python's lists support appending and popping in O(1), it is a perfect structure to use in implementing a stack. A stack class may be implemented using the following code. Carefully read the comments to understand each component of the stack.

```python
class Stack:
  """ Stack - implements key operations of the stack data structure

  Methods
  -------
  push(element)
    Adds an element to the stack.
  pop()
    Removes and returns the element on the top of stack.
  size()
    Returns the number of elements on stack.
  empty()
    Returns True if stack is empty. Otherwise, returns False.

  Attributes
  ----------
  stack : list
      A list to maintain the order of the elements on the stack
  """

  def __init__(self):
    # Initialize an empty list to store data on the stack
    self.stack = []
  
  def push(self, element):
    """Adds an element to the stack.

    Parameters
    ----------
    element : any
      The element to be added to the stack
    """
    # The push operation simply adds the element to the end of the list
    self.stack.append(element)

  def pop(self):
    """Removes and returns the element on the top of stack.
    
    Returns
    -------
    any
      the element from the top of the stack
    """
    # The list's pop method is perfect to remove the top of the stack
    return self.stack.pop()

  def size(self):
    """Returns the number of elements on stack.
    
    Returns
    -------
    int
      the number of elements on stack
    """
    # We can use the built in funciton to get size of the stack
    return len(self.stack)

  def empty(self):
    """Returns True if stack is empty. Otherwise, returns False.
    
    Returns
    -------
    boolean
      size == 0
    """
    # Simply return whether the size is equal to zero or not
    return self.size() == 0
```

## Stack Syntax

| Function      | Description                                                           | Python Syntax               |
| ---           | ---                                                                   | ---                         |
| push(element) | Adds an element to the top of the stack                               | my_stack_list.push(element) |
| pop()         | Removes the top element from the stack and returns it                 | my_stack_list.pop()         |
| size()        | Returns the number of elements on the stack                           | len(my_stack_list)          |
| empty()       | Returns **True** if the stack is empty. Otherwise, returns **False**. | len(my_stack_list) == 0     |

## Common Use Cases

In general, stacks are useful when a history needs to be retained such as in a browser application where the ability to navigate to previous pages is needed or as in a notepad tool which allows you to hit "undo" when you make a mistake. You may be familiar with the function stack which has important applications in programming allowing functions to call other functions and even supporting recursion. In fact, when your program crashes and an error is printed in the terminal, what is being shown is a trace of the stack to help you determine where the bug occured.

## Example Problem

Here is a simple example of using a stack to reverse a string

```python
# Using the Stack class defined above
myStack = Stack()

myString = "Hello World!"

# We iterate accross the string
for c in myString:
  # And add each character to the stack
  myStack.push(c)

newString = ""

# We will now loop for each character on the stack
for i in range(myStack.size()):
  # And add the character on top to our new string
  newString += myStack.pop()

# We've successfully reversed the string!
print(f"'{myString}' was changed to '{newString}'") # 'Hello World!' was changed to '!dlroW olleH'
```

Click [here](./solutions/stacks-example.py) to open a runnable python file.

## Tackle This

Implement a bracket checker using a stack. The bracket checker returns true if there is a closing bracket, ')', '}', or ']' for every opening bracket '(', '{', or '[' respectively. If a closing bracket of a different type is found then what is expected at that time, the bracket checker should return false. If there remains unpaired open brackets at the end of the process, the checker should return false.

Examples:
* 'Hello (world) [Welcome {All}]' -> Returns True
* 'Hello (world' -> Returns False
* 'Hello {[world}]' -> Returns False

You may use [my Stack class](./solutions/stack.py) for your stack implementation.

[Click here](./solutions/stacks-problem.py) to see the solution.