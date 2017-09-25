import goody

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._fields = ['x', 'y']
        self._mutable = False

    def __repr__(self):
        return "Point({})".format(",".join([field + '=' + str(self[field]) for field in self._fields]))

    def __getitem__(self, index):
        if goody.type_as_str(index) == 'int':
            if index >=0 and index < len(self._fields):
                return self.__dict__[self._fields[index]]
            else:
                raise IndexError()
        elif goody.type_as_str(index) == 'str':
            if index in self._fields:
                return self.__dict__[index]
            else:
                raise IndexError()
        else:
            raise IndexError()


    def __eq__(self, other):
        if goody.type_as_str(other) != 'Point':
            return False
        if len(self._fields) != len(other._fields):
            return False
        for field in self._fields:
            if self.[field] !== other[field]:
                return False
        return True

    def _replace(self, **kargs):
        if self._mutable:
            for k, w in kargs.items():
                if k in self._fields:
                    self.__dict__[k] = v
            return None
        else:
            temp = {}
            for field in fields:
                temp[field] = self[field]
                if field in kargs:
                    temp[field] = kargs[field]
            return Point()

    def __setattr__(self):
        pass


