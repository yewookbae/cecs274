import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
# import AdjacencyList
import MaxQueue
import time


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart.
    '''

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key,
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                b = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(b)
                self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
            # The following line is used to calculate the total time
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input:
            i: positive integer
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addsBookByKey(self, key):
        start_time = time.time()
        idx = self.bookIndices.find(key)
        if idx is not None:
            book = self.bookCatalog.get(idx)
            self.shoppingCart.add(book)
            print("Added title:", book.title)
        else:
            print("Book not found.")
        elapsed_time = time.time() - start_time
        print(f"addBookByKey Completed in {elapsed_time} seconds")

    def addBookByPrefix(self, pre: str):
        if pre != "":
            b_i = self.sortedTitleIndices.r_node(pre).v
            if b_i is not None:
                boo = self.bookCatalog.get(b_i)
                if len(boo.title) >= len(pre):
                    if boo.title[0:len(pre)] == pre:
                        self.shoppingCart.add(boo)
                        return boo.title
        return None

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i
        input:
            i: positive integer
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str):
        '''
        searchBookByInfix: Search all the books that contains infix
        input:
            infix: A string
        '''
        start_time = time.time()
        printed = 0
        n = self.bookCatalog.size()

        for i in range(n):
            book = self.bookCatalog.get(i)
            if infix in book.title:
                print("-" * 25)
                print(book)
                print()
                printed += 1
            if printed == 50:
                break
        print(f"Infix Matches: {printed}")
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shopping cart
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u}\nCompleted in {elapsed_time} seconds")

    def getCartBestSeller(self):
        '''
        removeFromShoppingCart: remove one book from the shopping cart
        '''
        s = time.time()
        print("getCartBestSeller returned")
        print(self.shoppingCart.max().title)
        e_time = time.time() - s
        print(f"Completed in {e_time} seconds")

    def bestsellers_with(self, infix, structure, n=0):

        """searches the book catalog for the first n books containing the given string infix,
        stores them in a data structure determined by structure,
        and prints them in order of highest ranking to lowest ranking"""

        # if infix is []:
        # print("Invalid infix.")
        # if structure is int(1):
        best_sellers = None
        if structure == 1:
            best_sellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2:
            best_sellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid data structure.")
        if best_sellers is not None:
            if infix == "":
                print("Invalid infix.")
            else:
                start_time = time.time()
                # FIXME: Insert the rest of the implementation here
                count = 0
                for i in range(self.bookCatalog.size()):
                    book = self.bookCatalog.get(i)
                    if infix in book.title:
                        if structure == 1:
                            best_sellers.add(book.rank, book)
                        else:
                            book.rank = (-1 * book.rank)
                            best_sellers.add(book)
                        count += 1
                        if count is n:
                            break
                if structure == 1:
                    b_s = reversed(best_sellers.in_order())
                    for book in b_s:
                        print(book.v)
                        print()
                else:
                    while best_sellers.size() > 0:
                        book = best_sellers.remove()
                        book.rank = (-1 * book.rank)
                        print(book)
                elapsed_time = time.time() - start_time
                print(f"Displayed bestsellers_with(\"{infix}\", {structure}, {n}) in {elapsed_time} seconds")

    # def sort_catalog(self, s):
    # start_time = time.time()
    # elapsed_time = time.time() - start_time
    # if s == 1:
    #    algorithms.merge_sort(self.bookCatalog)
    #    print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")
    #    return True
    # elif s == 2:
    #    algorithms._quick_sort_f(self.bookCatalog, 0, len(self.bookCatalog)-1)
    #    #print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")
    #    return True
    # elif s == 3:
    #   algorithms._quick_sort_r(self.bookCatalog, 0, len(self.bookCatalog)-1)
    #   print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")
    #   return True
    # else:
    #   return False

    # def display_catalog(self, n):
    #   for i in range(n):
    #      if i >= len(self.bookCatalog):
    #         break
    #    print(self.bookCatalog[i])