from .stack import Stack

class Node:
    def __init__(self, an_object=None):
        self._item = an_object
        self.next = None

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, an_item):
        self._item = an_item


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        if not isinstance(node, Node):
            raise TypeError("Invalid inputs")

        node.next = None
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete(self, value):
        current = self.head
        prev = None
        found = False

        while current:
            if current.item == value:
                found = True
                break

            prev = current
            current = current.next

        if found and prev:
            prev.next = current.next
        if found and not prev:
            self.head = self.head.next

    def __contains__(self, item):
        current = self.head
        found = False

        while current:
            if current.item == item:
                found = True
                break
            current = current.next
        return found

    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def clear(self):
        self.head = None
        self.tail = None

    def reverse(self):
        s = Stack(len(self))
        current = self.head
        while current:
            s.push(current)
            current = current.next

        self.clear()
        while True:
            self.insert(s.pop())
            if len(s) == 0:
                break

    def __str__(self):
        lst = []
        current = self.head
        while current:
            lst.append(str(current.item))
            current = current.next

        return '-'.join(lst)



