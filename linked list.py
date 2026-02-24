class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None
            
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0
    
    def add(self, element):
        node = self.Node(element)
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1
    
    def remove(self, element):
        current_node = self.head
        previous_node = None
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next