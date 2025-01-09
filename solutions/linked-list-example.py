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

if __name__ == '__main__':
    # Test cases
    print(is_palindrome('racecar'))  # True
    print(is_palindrome('hello'))    # False
    print(is_palindrome('Hannah'))   # True