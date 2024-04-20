class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__ (self):
        self.head = None

    def InsertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node


    def printLL(self) -> str:
        current_node = self.head
        strr =''
        while (current_node):
            strr+= current_node.data + '\n'
            current_node = current_node.next
        return strr




