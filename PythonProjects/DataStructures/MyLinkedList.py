class LinkedList:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.count = 0

    def prepend(self, value):
        self.head = LinkedList.Node(value, self.head)
        self.count += 1

    def __len__(self):
        return self.count

    def __iter__(self):
        n = self.head
        while n:
            yield n.val
            n = n.next

    def __repr__(self):
        return '[' + ', '.join(str(x) for x in self) + ']'

class DoublyLinkedList:
    class Node:
        def __init__(self, val, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next  = next

    def __init__(self):
        self.head = LinkedList.Node(None) # *sentinel* node!
        self.head.prev = self.head.next = self.head
        self.count = 0

    def prepend(self, value):
        n = LinkedList.Node(value, prev=self.head, next=self.head.next)
        # important: Python carries out multiple assignments from *left to right*!
        self.head.next.prev = self.head.next = n
        self.count += 1

    def append(self, value):
        n = LinkedList.Node(value, prev=self.head.prev, next=self.head)
        n.prev.next = n.next.prev = n
        self.count += 1

    def del_head(self):
        assert(len(self) > 0)
        to_del = self.head.next
        # note: following is location agnostic!
        to_del.prev.next = to_del.next
        to_del.next.prev = to_del.prev
        self.count -= 1

    def __len__(self):
        return self.count

    def __iter__(self):
        n = self.head.next
        while n is not self.head:
            yield n.val
            n = n.next

    def __repr__(self):
        return '[' + ', '.join(str(x) for x in self) + ']'
