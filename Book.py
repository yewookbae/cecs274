class Book:
    '''
    Class: Book contains the detail of the books. It allows comparing
    two instances according to the title (in alphabetical order Aa - Zz).
    '''

    def __init__(self, key, title, group, rank, similar):
        self.key = key
        self.title = title
        self.group = group
        self.rank = int(rank)
        self.similar = similar

    def __lt__(self, other):
        '''
        This function allows to make direct comparation using the operator <
        '''
        return self.title.lower() < other.title.lower()

    def __gt__(self, other):
        '''
        This function allows to make direct comparation using the operator >
        '''
        return self.title.lower() > other.title.lower()

    def __le__(self, other):
        '''
        This function allows to make direct comparation using the operator <=
        '''
        return self.title.lower() <= other.title.lower()

    def __ge__(self, other):
        '''
        This function allows to make direct comparation using the operator >=
        '''
        return self.title.lower() >= other.title.lower()

    def __eq__(self, other):
        '''
        This function allows to make direct comparation using the operator ==
        '''
        return self.title.lower() == other.title.lower() and self.key == other.key

    def __str__(self):
        '''
        function returns a string containing the book information
        '''
        return f"\n\tBook: {self.key}\n\tTitle: {self.title}\n\tGroup: {self.group}\n\tRank: {self.rank}"

