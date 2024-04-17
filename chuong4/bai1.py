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

    def print_reverse_recursive(self, node):
        if node is None:
            return
        self.print_reverse_recursive(node.next)
        print(node.info, end=" ")

    def print_reverse_non_recursive(self):
        if self.head is None:
            return
        
        stack = []
        current = self.head

        # Push nodes onto the stack
        while current is not None:
            stack.append(current)
            current = current.next

        # Pop and print nodes from the stack
        while stack:
            node = stack.pop()
            print(node.info, end=" ")

# Test the LinkedList class
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_at_beginning(1)
    linked_list.add_at_beginning(2)
    linked_list.add_at_beginning(3)
    linked_list.add_at_beginning(4)
    linked_list.add_at_beginning(5)

    print("Original linked list:")
    current = linked_list.head
    while current is not None:
        print(current.info, end=" ")
        current = current.next

    print("\n\nPrinting the linked list in reverse using recursion:")
    linked_list.print_reverse_recursive(linked_list.head)

    print("\n\nPrinting the linked list in reverse using a stack (non-recursive):")
    linked_list.print_reverse_non_recursive()
