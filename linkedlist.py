from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def depend_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            node.next = self.head
            self.head = node

    def contains_node(self, data):
        temporary_node = self.head
        while temporary_node.next is not None:
            if temporary_node.data == data:
                print('True')
                return True
            temporary_node = temporary_node.next
        print("False")

