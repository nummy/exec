# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        if not self.head:
            return
        Odd_L = ExtendedLinkedList()
        Even_L = ExtendedLinkedList()
        while self.head:
            node = self.head
            self.head = node.next_node
            if node.value%2 != 0:
                node.next_node = None
                if not Odd_L.head:
                    Odd_L.head = node
                else:
                    o_node = Odd_L.head
                    while o_node.next_node:
                        o_node = o_node.next_node
                    o_node.next_node = node
            else:
                node.next_node = None
                if not Even_L.head:
                    Even_L.head = node
                else:
                    e_node = Even_L.head
                    while e_node.next_node:
                        e_node = e_node.next_node
                    e_node.next_node = node
        Odd_L.extend(Even_L)
        self.head = Odd_L.head


