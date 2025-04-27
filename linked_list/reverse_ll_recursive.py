class NOde:
    def __init__(self , data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def reverse(self):
        if self.head is None:
            return None
        return self.reverse_util(self.head)
    
    def reverse_util(self, node):
        if node.next is None:
            self.head = node
            return node
        prev = self.reverse_util(node.next)
        prev.next = node
        node.next = None
        return node
    
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