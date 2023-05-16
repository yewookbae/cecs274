import numpy as np
import math
import SLLQueue
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    # todo

    return 2 * i + 1

    # pass


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    # todo

    return 2 * (i + 1)

    # pass


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    # todo

    return (i - 1) // 2

    # pass


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        # todo

        if len(self.a) == self.n:
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True

        # pass

    def remove(self):
        # todo

        if self.n == 0:
            raise IndexError
        x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n -= 1
        self._trickle_down_root()
        #if (3 * self.n) < len(self.a):
            #self._resize()
        return x

        # pass

    def depth(self, u) -> int:
        # todo

        """Returns the integer depth of element u in the binary heap.
        If u is not found in the binary heap, raises a ValueError
        with the message "<u> is not found in the binary tree."""

        for i in range(self.n):
            if self.a[i] is u:
                return math.floor(math.log2(i + 1))
        raise ValueError(f"{u} is not found in the binary tree.")

        # pass

    def height(self) -> int:
        # todo

        """Returns the height of the binary heap.
        The worse case runtime is O(n)."""

        return math.floor(math.log2(self.n))

        # pass

    def bf_order(self) -> list:
        # todo

        if self.n == 0:
            return []
        r = []
        q = [0]

        while q:
            i = q.pop(0)
            r.append(self.a[i])
            left_index = left(i)
            right_index = right(i)

            if left_index < self.n:
                q.append(left_index)
            if right_index < self.n:
                q.append(right_index)
        return r

        # pass

    """Returns the list of values in the binary heap as they are traversed
            using the in-order traversal."""

    def in_order(self) -> list:
        # todo

        return self._in_order(0)

    def _in_order(self, i):

        n = []
        if left(i) < self.n:
            n.extend(self._in_order(left(i)))
        n.append(self.a[i])
        if right(i) < self.n:
            n.extend(self._in_order(right(i)))
        return n

        # pass

    def post_order(self) -> list:
        # todo

        """Returns the list of values in this binary heap as they are
        traversed using the in-order traversal."""

        res = []
        self._post_order(0, res)
        return res

    def _post_order(self, i, res):

        if i < len(self):
            left_idx = left(i)
            right_idx = right(i)
            self._post_order(left_idx, res)
            self._post_order(right_idx, res)
            res.append(self.a[i])

        # pass

    def pre_order(self) -> list:
        # todo

        """ returns the list of values in this binary heap as they are traversed using the in-order traversal."""

        return self._pre_order(0)

    def _pre_order(self, i):

        n = []
        n.append(self.a[i])
        if left(i) < self.n:
            n.extend(self._pre_order(left(i)))
        if right(i) < self.n:
            n.extend(self._pre_order(right(i)))
        return n

        # pass

    def find_min(self):
        if self.n == 0:
            raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        # todo

        i = self.n - 1
        p_idx = parent(i)
        while i > 0 and self.a[i] < self.a[p_idx]:
            self.a[i], self.a[p_idx] = self.a[p_idx], self.a[i]
            i = p_idx
            p_idx = parent(i)
        # pass

    def size(self) -> int:
        return self.n

    def _resize(self):
        # todo

        """ resizes the backing array a to maintain the invariant n ≤ len(a) ≤ 3n"""

        new = _new_array(2 * self.n)
        for i in range(self.n):
            new[i] = self.a[i]
        self.a = new

        # pass

    def _trickle_down_root(self):
        # todo

        i = 0
        left_index = left(i)
        right_index = right(i)
        while ((i < self.n and (left_index < self.n or right_index < self.n)) and
               (self.a[i] > self.a[left_index] or self.a[i] > self.a[right_index])):
            min_index = i
            if left_index < self.n:
                if self.a[left_index] < self.a[i]:
                    min_index = left_index
                else:
                    min_index = i
            if right_index < self.n:
                if self.a[right_index] < self.a[min_index]:
                    min_index = right_index
            self.a[i], self.a[min_index] = self.a[min_index], self.a[i]
            i = min_index
            left_index = left(i)
            right_index = right(i)

        # pass

    def __str__(self):
        return str(self.a[0:self.n])