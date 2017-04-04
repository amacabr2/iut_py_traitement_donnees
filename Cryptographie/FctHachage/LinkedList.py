"""
Auteur: Cette classe a été trouvé sur le net
"""


class LinkedList:
    def __init__(self, root):
        self.root = root
        self.tail = root

    def toString(self):
        s = ""
        root = self.root

        if root == None:
            return s

        while (root != None):
            s += root.value
            root = root.next
        return s

    def add(self, node):
        if self.root == None:
            self.root = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


class Node:
    """A simple node for the list"""

    def __init__(self, value, next):
        self.value = value
        self.next = next
