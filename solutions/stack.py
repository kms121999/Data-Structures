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
    