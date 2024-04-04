# Import the stack class from the stack.py file
from stack import Stack
    
if __name__ == "__main__":
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
    