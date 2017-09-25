from collections import defaultdict
from goody import type_as_str

class Bag:
    def __init__(self, iterable=[]):
        self.data = defaultdict(int)
        for i in iterable:
            self.data[i] = self.data.get(i,0) + 1

    def __repr__(self):
        arr = []
        for k, v in self.data.items():
            arr.extend([k]*v)
        return "Bag(%s)" % repr(arr)

    def __str__(self):
        arr = []
        for k, v in self.data.items():
            arr.append("%s[%d]" % (k,v))
        return "Bag(%s)" % ",".join(arr)


    def __len__(self):
        length = 0
        for k, v in self.data.items():
            length += v;
        return length

    def unique(self):
        return len(self.data)

    def __contains__(self, value):
        return value in self.data

    def count(self, value):
        return self.data.get(value, 0)
    

    def add(self, value):
        self.data[value] = self.data.get(value, 0) + 1


    def __add__(self, other):
        arr = []
        for k, v in self.data.items():
            for i in range(v):
                arr.append(k)
        if isinstance(other, Bag):
            for k, v in other.data.items():
                for i in range(v):
                    arr.append(k)
            return Bag(arr)
        else:
            raise TypeError("%s is not a instance of Bag" % str(other))
        


    def remove(self, value):
        if value in self.data:
            if self.data[value] == 1:
                del self.data[value]
            else:
                self.data[value] = self.data[value] - 1
        else:
            raise ValueError("%s is not in the Bag" % value)

    def __eq__(self, other):
        if not isinstance(other, Bag):
            return False
        else:
            if self.data == other.data:
                return True
            else:
                return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iter__(self):
        arr = []
        for k, v in self.data.items():
            for i in range(v):
                arr.append(k)
        return iter(arr)
    





if __name__ == '__main__':
    #Put your own test code here to test Bag before doing bsc tests

    print('Start simple testing')

    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
#     driver.default_show_traceback =True
    driver.driver()
