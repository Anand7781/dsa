class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None

class LL:
    def __init__(self):
        self.head = None  

    def remove_nth_element(self, n):
        length = 0
        temp = self.head

        while temp:
            length += 1
            temp = temp.next

        if n > length or n <= 0:
            raise ValueError("Invalid value of n")

        k = length - n
        i = 0
        prev = None
        curr = self.head

        
        while i < k:  
            prev = curr
            curr = curr.next
            i += 1

        
        if prev is None:
            self.head = self.head.next
            return self.head

       
        prev.next = curr.next

        return self.head
    




