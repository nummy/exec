import prompt,re
import math
from goody import type_as_str

class Point:
    def __init__(self, x, y, z):
        assert isinstance(x,int) is True
        assert isinstance(y,int) is True
        assert isinstance(z,int) is True
        self.x = x
        self.y = y
        self.z = z


    def __str__(self):
        return "(x=%s,y=%s,z=%s)" % (self.x, self.y, self.z)

    def __repr__(self):
        return "Point(%s,%s,%s)" % (self.x, self.y, self.z)

    def __bool__(self):
        if self.x == 0 and self.y == 0 and self.z == 0:
            return False
        else:
            return True

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError("the right operand is not a instance of Point")
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x,y,z)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("%s is not a int" % other)
        return Point(self.x*other, self.y*other, self.z*other)

    def __rmul__(self,other):
        if not isinstance(other, int):
            raise TypeError("%s is not a int" % other)
        return Point(self.x*other, self.y*other, self.z*other)

    def __lt__(self, other):
        distance = (self.x**2+self.y**2+self.z**2)**0.5
        if isinstance(other,(int,float)):
            if distance < other:
                return True
            else:
                return False
        elif isinstance(other,Point):
            distance2 = (other.x**2+other.y**2+other.z**2)**0.5
            if distance < distance2:
                return True
            else:
                return False
        else:
            raise TypeError("other should be Point object or number")

    def __getitem__(self, index):
        if index == "x" or index is 0:
            return self.x
        elif index == "y" or index is 1:
            return self.y
        elif index == "z" or index is 2:
            return self.z
        else:
            raise IndexError("%s should be 'x|y|z|0|1|2'")

    def __call__(self, x, y, z):
        assert isinstance(x,int) is True
        assert isinstance(y,int) is True
        assert isinstance(z,int) is True
        self.x = x
        self.y = y
        self.z = z
        return None


if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test Point before doing bsc tests
    print('Start simple testing')
    print()
    import driver
    
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
