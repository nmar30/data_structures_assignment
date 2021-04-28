from binarytreenode import BinaryTreeNode


class BinaryTree:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = BinaryTreeNode(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        elif node.data < self.tail.data:
            self.tail.left = node
            self.tail.right = None
            self.tail = self.tail.left
        elif node.data > self.tail.data:
            self.tail.right = node
            self.tail.left = None
            self.tail = self.tail.right

    # def contains_node(self, data):
    #     temporary_node = self.head
    #     while temporary_node is not None:
    #         if temporary_node.data == data:
    #             print('True')
    #             return True
    #     print("False")
