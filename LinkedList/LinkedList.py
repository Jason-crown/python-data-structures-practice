
class Node:
    """Represents a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Implements a singly linked list."""
    def __init__(self):
        self.head = None

    # Add a node to the end
    def append(self, data):
        """Adds a new node to the end of the list."""
        new_node = Node(data)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            return

        # Find the last node
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    # Print every node
    def display(self):
        """Prints all nodes in the list."""
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # Search for a value
    def search(self, target):
        """Searches for a node with the given value."""
        current = self.head

        while current is not None:
            if current.data == target:
                return True
            current = current.next

        return False

    # Delete the first node with the given value
    def delete(self, target):
        """Deletes the first node with the given value."""
        current = self.head

        # Handle deletion of the head
        if current is not None and current.data == target:
            self.head = current.next
            return True

        # Find the node before the target
        while current is not None and current.next is not None:
            if current.next.data == target:
                current.next = current.next.next
                return True

            current = current.next

        return False


# Test the linked list
my_list = LinkedList()

my_list.append(10)
my_list.append(20)
my_list.append(30)

my_list.display()
# 10 -> 20 -> 30 -> None

print(my_list.search(20))
# True

my_list.delete(20)
my_list.display()
# 10 -> 30 -> None
