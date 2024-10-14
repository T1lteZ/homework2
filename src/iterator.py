class TaskIterator:

    def __init__(self, prod):
        self.category = prod
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.list_prod):
            new = self.category.list_prod[self.index]
            self.index += 1
            return new
        else:
            raise StopIteration
