class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, info):
        new_node = Node(info)
        new_node.next = self.head
        self.head = new_node

    def dao_nguoc(self):
        if self.head is None or self.head.next is None:
            return
        
        stack = []
        current = self.head

        # Push nodes onto the stack
        while current is not None:
            stack.append(current)
            current = current.next
        
        # Set the head to the last node
        self.head = stack[-1]
        current = self.head

        # Pop nodes from the stack and update pointers
        while stack:
            node = stack.pop()
            current.next = node
            current = current.next
        current.next = None

    def display(self):
        current = self.head
        while current is not None:
            print(current.info, end=" ")
            current = current.next
        print()

# Test the LinkedList class
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_at_beginning(1)
    linked_list.add_at_beginning(2)
    linked_list.add_at_beginning(3)
    linked_list.add_at_beginning(4)
    linked_list.add_at_beginning(5)

    print("Original linked list:")
    linked_list.display()

    print("Reversed linked list:")
    linked_list.dao_nguoc()
    linked_list.display()
