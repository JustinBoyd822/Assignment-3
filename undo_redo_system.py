from node import Node

class Stack:
    """
    A custom Stack implementation using linked nodes.
    Follows LIFO (Last In, First Out) principle.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self.top = None
    
    def push(self, value):
        """
        Add a new node with the given value to the top of the stack.
        
        Args:
            value: The value to add to the stack
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        """
        Remove and return the value from the top of the stack.
        
        Returns:
            The value from the top node, or None if stack is empty
        """
        if self.top is None:
            return None
        
        value = self.top.value
        self.top = self.top.next
        return value
    
    def peek(self):
        """
        Return the value at the top of the stack without removing it.
        
        Returns:
            The value from the top node, or None if stack is empty
        """
        if self.top is None:
            return None
        return self.top.value
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            True if stack is empty, False otherwise
        """
        return self.top is None
    
    def print_stack(self):
        """Print all values in the stack from top to bottom."""
        if self.is_empty():
            print("Stack is empty")
            return
        
        current = self.top
        while current:
            print(f"- {current.value}")
            current = current.next

def main():
    """Main function to run the Undo/Redo Manager CLI."""
    print("--- Undo/Redo Manager ---")
    
    # Create two stacks for undo/redo functionality
    undo_stack = Stack()
    redo_stack = Stack()
    
    while True:
        print("\n1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            # Perform action
            action = input("Describe the action (e.g., Insert 'a'): ").strip()
            if action:
                undo_stack.push(action)
                # Clear redo stack when new action is performed
                redo_stack = Stack()
                print(f"Action performed: {action}")
            else:
                print("Please enter a valid action description.")
        
        elif choice == "2":
            # Undo
            action = undo_stack.pop()
            if action is not None:
                redo_stack.push(action)
                print(f"Undid action: {action}")
            else:
                print("No actions to undo")
        
        elif choice == "3":
            # Redo
            action = redo_stack.pop()
            if action is not None:
                undo_stack.push(action)
                print(f"Redid action: {action}")
            else:
                print("No actions to redo")
        
        elif choice == "4":
            # View Undo Stack
            print("Undo Stack:")
            undo_stack.print_stack()
        
        elif choice == "5":
            # View Redo Stack
            print("Redo Stack:")
            redo_stack.print_stack()
        
        elif choice == "6":
            # Exit
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please select 1-6.")

if __name__ == "__main__":
    main()
