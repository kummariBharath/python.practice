# Linked List Implementation

This document provides a step-by-step explanation of the Singly Linked List implementation found in `linked list.py`.

## 1. Class Structure

### The `LinkedList` Class
This is the main class that manages the list. It keeps track of the first node (`head`) and the total number of elements (`length`).

### The Nested `Node` Class
Inside `LinkedList`, there is a helper class called `Node`.
```python
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
```
*   **`element`**: Stores the actual data (e.g., an integer).
*   **`next`**: Stores a reference (link) to the next node in the sequence. It defaults to `None`.

---

## 2. Methods Breakdown

### Initialization: `__init__`
```python
def __init__(self):
    self.length = 0
    self.head = None
```
*   Initializes an empty list.
*   **`head`**: Points to `None` because there are no nodes yet.
*   **`length`**: Starts at 0.

### Check Status: `is_empty`
```python
def is_empty(self):
    return self.length == 0
```
*   Returns `True` if the list has 0 elements, otherwise `False`.

### Adding Items: `add`
Adds a new element to the **end** of the list.
```python
def add(self, element):
    node = self.Node(element)      # 1. Create a new Node
    if self.is_empty():
        self.head = node           # 2. If list is empty, new node is the head
    else:
        current_node = self.head   # 3. Start at the beginning
        while current_node.next is not None: # 4. Traverse to the end
            current_node = current_node.next
        current_node.next = node   # 5. Link the last node to the new node
    self.length += 1               # 6. Increase length count
```

### Removing Items: `remove`
Removes the first occurrence of a specific value.
```python
def remove(self, element):
    previous_node = None
    current_node = self.head
    
    # 1. Search for the node
    while current_node is not None and current_node.element != element:
        previous_node = current_node
        current_node = current_node.next
    
    # 2. Handle case where item is not found
    if current_node is None:
        return        
    
    # 3. Handle case where item is in the middle or end
    elif previous_node is not None:
        previous_node.next = current_node.next
        
    # 4. Handle case where item is at the head
    else:
        self.head = current_node.next
        
    self.length -= 1  # 5. Decrease length count
```

---

## 3. Usage Example
The code at the bottom of the file demonstrates how to use the class:

```python
my_list = LinkedList()    # Create instance
print(my_list.is_empty()) # Check if empty (True)

my_list.add(1)            # Add 1
my_list.add(2)            # Add 2
print(my_list.is_empty()) # Check if empty (False)
print(my_list.length)     # Check length (2)
```