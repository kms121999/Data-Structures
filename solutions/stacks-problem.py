# Import the stack class from the stack.py file
from stack import Stack

def check_brackets(text):
    # Using the Stack class defined above
    myStack = Stack()

    # Iterate accross the string
    for c in text:
        # If the character is an opening bracket, add it to the stack
        if c in "([{":
            myStack.push(c)
        # If the character is a closing bracket, check if it was expected
        elif c in ")]}":
            # If the stack is empty, there is no opening bracket to match
            if myStack.empty():
                return False
            # If the closing bracket does not match the paired opening bracket, return False
            top = myStack.pop()
            if c == ")" and top != "(":
                return False
            if c == "]" and top != "[":
                return False
            if c == "}" and top != "{":
                return False
    
    # If the stack is not empty, there are unmatched opening brackets
    return myStack.empty()


if __name__ == "__main__":
    # Test cases
    print(check_brackets("Hello (world) [Welcome {All}]")) # True
    print(check_brackets("Hello (world")) # False
    print(check_brackets("Hello {[world}]")) # False