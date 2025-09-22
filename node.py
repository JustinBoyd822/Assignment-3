class Node:
    """
    A Node class for use in linked list-based data structures.
    Each node contains a value and a pointer to the next node.
    """
    
    def __init__(self, value):
        """
        Initialize a new Node with the given value.
        
        Args:
            value: The data to store in this node
        """
        self.value = value
        self.next = None
