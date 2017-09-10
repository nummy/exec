class Permutation(object):
    
    def __init__(self, length=0, numbers=[]):
        self.length = length
        self.numbers = numbers or range(1, self.length + 1)
        self.nb_of_cycle = 0

    def __len__(self):
        pass

    def __repr__(self):
        return 'Permutation(length=%s, numbers=%s)' % (self.length, self.numbers)

    def __str__(self):
        return self.___repr__()

    def inverse(self):
        pass

    def __mul__(self):
        pass
