from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
              #edited
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        # todo
        if i < 0 or i >= self.n:
            return self.dummy   #edited
        if i < self.n/2:
            p = self.dummy.next
            for _ in range(i):
                p = p.next
        else:
            p = self.dummy
            for _ in range(self.n-1, i - 1, -1):
                p = p.prev
        return p

    def get(self, i) -> object:
        # todo
        if i < 0 or i >= self.n:
            raise IndexError
        return self.get_node(i).x  #correct?

    def set(self, i: int, x: object) -> object:
        # todo
        if i < 0 or i >= self.n:
            raise IndexError
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w: Node, x: object) -> Node:
        # todo
        if w is None:
            raise IndexError
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        w.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i: int, x: object):
        # todo
        if i < 0 or i > self.n:
            raise IndexError
        return self.add_before(self.get_node(i), x)

    def _remove(self, w: Node):
        # todo
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x

    def remove(self, i: int):
        if i >= self.n:     #edited
            raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        # todo
        left = self.dummy.next
        right = self.dummy.prev
        for i in range(int(self.n//2)):
            if left.x != right.x:
                return False
            left = left.next
            right = right.prev
        return True

    def reverse(self):
        head = self.dummy.next
        tail = self.dummy.prev
        for _ in range(int(self.n / 2)):
            temp_holder = head.x
            head.x = tail.x
            tail.x = temp_holder
            head = head.next
            tail = tail.prev


    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
