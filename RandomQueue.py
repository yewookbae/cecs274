import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        # todo
        if self.n < 1:
            raise IndexError()
        i = random.randint(0, (self.n - 1))
        j = self.a[self.j % len(self.a)]
        removed_e = self.a[(self.j + i) % len(self.a)]

        self.a[(self.j + i) % len(self.a)] = j
        self.a[self.j] = removed_e

        return super().remove()



