# Node class represents each element in the linked list
class Node:
    def __init__(self, data=None):
        self.data = data  # stores the data
        self.next = None  # stores the reference to the next node

# LinkedList class represents the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # initially, the list is empty

    # Method to append a new node to the end of the list
    def append(self, data):
        new_node = Node(data)  # create a new node with the given data
        if self.head is None:
            self.head = new_node  # if the list is empty, the new node becomes the head
        else:
            current = self.head
            while current.next:  # traverse to the end of the list
                current = current.next
            current.next = new_node  # add the new node at the end

    # Method to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to insert a node at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  # new node points to the current head
        self.head = new_node  # new node becomes the head

    # Method to delete a node with a specific value
    def delete_node(self, key):
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next  # move the head to the next node
            current = None  # free the old head
            return

        # Search for the node to be deleted
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next

        # If the node was not found
        if current is None:
            return

        # Unlink the node from the linked list
        previous.next = current.next
        current = None

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()  # Output: 1 -> 2 -> 3 -> None

ll.prepend(0)
ll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None

ll.delete_node(2)
ll.print_list()  # Output: 0 -> 1 -> 3 -> None