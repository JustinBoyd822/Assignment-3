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



#DESIGN MEMO: Data Structure Selection and Implementation Analysis

#Why is a stack the right choice for undo/redo?

#A stack is the perfect data structure for undo/redo functionality because it follows the LIFO (Last In, First Out) principle, which exactly matches how users expect undo/redo to work. When a user performs actions sequentially and then wants to undo them, they expect the most recent action to be undone first, then the second-most recent, and so on. This is precisely how a stack operates – the last item pushed onto the stack is the first item popped off. The two-stack approach (undo_stack and redo_stack) elegantly handles both directions: actions move from undo to redo when undoing, and back to undo when redoing.

#Why is a queue better suited for the help desk?

#A queue is ideal for the help desk system because it implements FIFO (First In, First Out) ordering, ensuring fairness in customer service. Customers who arrive first should be helped first, which is exactly how queues work. This prevents any customer from being unfairly bypassed and maintains the expected "wait your turn" behavior that users understand from real-world queuing systems.

#How do your implementations differ from Python's built-in lists?

#Our custom implementations use linked nodes rather than contiguous memory arrays. While Python lists offer O(1) access to any element by index, our structures sacrifice this random access for more memory-efficient operations at specific positions. Our stack only needs O(1) operations at the top, and our queue only needs O(1) operations at front and rear. Python lists would require O(n) operations for queue-like behavior when removing from the front, making our custom queue more efficient for this specific use case. Additionally, our implementations enforce the intended access patterns (LIFO/FIFO) whereas Python lists allow arbitrary insertions and deletions that could break the logical structure.
