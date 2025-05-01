class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def find_loop(self):
        current = self.head
        pointers = {}
        index = 0

        while current:
            if current not in pointers:
                pointers[current] = index
                index += 1
                current = current.next
            else:
                # Loop detected
                return True
        return False
    
    def printll(self):
        temp = self.head
        visited = set()
        while temp:
            if temp in visited:
                print("Loop detected. Stopping print to avoid infinite loop.")
                break
            print(temp.data)
            visited.add(temp)
            temp = temp.next


            

