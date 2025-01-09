from collections import deque

def rotate_linked_list(linked_list, rotation_amount):
    rotation_amount = (len(linked_list) + rotation_amount % len(linked_list)) % len(linked_list)
    
    for _ in range(rotation_amount):
        linked_list.appendleft(linked_list.pop())
        
    return linked_list

if __name__ == '__main__':
    # Test cases
    linked_list = deque([1, 2, 3, 4, 5])
    print(rotate_linked_list(linked_list, 2))  # deque([4, 5, 1, 2, 3])
    
    linked_list = deque([1, 2, 3, 4, 5])
    print(rotate_linked_list(linked_list, -2))  # deque([3, 4, 5, 1, 2])
    
    linked_list = deque([1, 2, 3, 4, 5])
    print(rotate_linked_list(linked_list, 7))  # deque([4, 5, 1, 2, 3])
    
    linked_list = deque([1, 2, 3, 4, 5])
    print(rotate_linked_list(linked_list, -7))  # deque([3, 4, 5, 1, 2])
    
    linked_list = deque([1, 2, 3, 4, 5])
    print(rotate_linked_list(linked_list, 0))  # deque([1, 2, 3, 4, 5])
    
    linked_list = deque([1, 2, 3, 4, 5])
    print(rotate_linked_list(linked_list, 5))  # deque([1, 2, 3, 4, 5])
    
    linked_list = deque([1, 2, 3, 4, 5])
    print(rotate_linked_list(linked_list, -5))  # deque([1, 2, 3, 4, 5])