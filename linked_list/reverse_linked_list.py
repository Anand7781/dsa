class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nrext_node = current.next  # Store next node
            current.next = prev
            prev = current
            current = nrext_node
        self.head = prev
        return self.head
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    ll = LL()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)

    print("Original Linked List:")
    ll.print_list()

    ll.reverse()

    print("Reversed Linked List:")
    ll.print_list()