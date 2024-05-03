class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def InsertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def printLL(self) -> str:
        current_node = self.head
        string = ''
        while current_node:
            string += current_node.data + '\n'
            current_node = current_node.next
        return string

    def print_i_elem(self, i):
        curr = self.head
        count = 0
        while curr:
            if count == i:
                return curr.data
            count += 1
            curr = curr.next
        print("index out of range")







