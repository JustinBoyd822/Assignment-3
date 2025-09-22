from node import Node

class Queue:
    """
    A custom Queue implementation using linked nodes.
    Follows FIFO (First In, First Out) principle.
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        """
        Add a new node with the given value to the rear of the queue.
        
        Args:
            value: The value to add to the queue
        """
        new_node = Node(value)
        
        if self.rear is None:
            # Queue is empty, both front and rear point to new node
            self.front = new_node
            self.rear = new_node
        else:
            # Add to the rear and update rear pointer
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        """
        Remove and return the value from the front of the queue.
        
        Returns:
            The value from the front node, or None if queue is empty
        """
        if self.front is None:
            return None
        
        value = self.front.value
        self.front = self.front.next
        
        # If queue becomes empty, also update rear
        if self.front is None:
            self.rear = None
        
        return value
    
    def peek(self):
        """
        Return the value at the front of the queue without removing it.
        
        Returns:
            The value from the front node, or None if queue is empty
        """
        if self.front is None:
            return None
        return self.front.value
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            True if queue is empty, False otherwise
        """
        return self.front is None
    
    def print_queue(self):
        """Print all values in the queue from front to rear."""
        if self.is_empty():
            print("Queue is empty")
            return
        
        current = self.front
        while current:
            print(f"- {current.value}")
            current = current.next

def main():
    """Main function to run the Help Desk Ticketing System CLI."""
    print("--- Help Desk Ticketing System ---")
    
    # Create queue for managing customer tickets
    queue = Queue()
    
    while True:
        print("\n1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            # Add customer
            name = input("Enter customer name: ").strip()
            if name:
                queue.enqueue(name)
                print(f"{name} added to the queue.")
            else:
                print("Please enter a valid customer name.")
        
        elif choice == "2":
            # Help next customer
            customer = queue.dequeue()
            if customer is not None:
                print(f"Helped: {customer}")
            else:
                print("No customers waiting in the queue.")
        
        elif choice == "3":
            # View next customer
            next_customer = queue.peek()
            if next_customer is not None:
                print(f"Next customer: {next_customer}")
            else:
                print("No customers waiting in the queue.")
        
        elif choice == "4":
            # View all waiting customers
            print("Waiting customers:")
            queue.print_queue()
        
        elif choice == "5":
            # Exit
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main()
