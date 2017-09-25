from goody import irange, type_as_str
import math
import inspect

class Rational:
    def __init__(self, numerator=0, denominator=1):
        if type_as_str(numerator) != "int":
            raise AssertionError("Rational.__init__ numerator is not int: %s" % numerator)
        if type_as_str(denominator) != "int":
            raise AssertionError("Rational.__init__ denominator is not int: %s" % denominator)
        if denominator == 0:
            raise AssertionError("Rational.__init__ denominator can not be zero: %s" % denominator)
        gcd = self._gcd(abs(numerator), abs(denominator))
        self.num = numerator*denominator//(gcd*abs(denominator))
        self.denom = abs(denominator)//gcd

    def __str__(self):
        return "%s/%s" % (self.num, self.denom)

    def __repr__(self):
        return "Rational(%s,%s)" % (self.num, self.denom)

    def __add__ (self, other):  
        #Add two rational numbers. 
        self._validate_arithmetic(other,{Rational,int},'+','Rational',type_as_str(other))
        if type_as_str(other) == "int":
            other = Rational(other, 1)
        print(self.num*other.denom + other.num * self.denom)
        return Rational(self.num*other.denom + other.num * self.denom,  self.denom * other.denom)

    def __radd__ (self, other):  
        return self.__add__(other)

    def __sub__ (self, other):
        self._validate_arithmetic(other,{Rational,int},'-','Rational',type_as_str(other))
        if type_as_str(other) == "int":
            other = Rational(other, 1)
        return Rational(self.num*other.denom - other.num * self.denom,  self.denom * other.denom)

    def __rsub__(self, other):
        self._validate_arithmetic(other,{Rational,int},'*','Rational',type_as_str(other))
        if type_as_str(other) == "int":
            other = Rational(other, 1)
        return Rational(other.num * self.denom - self.num*other.denom,  self.denom * other.denom)

    def __mul__(self, other):
        self._validate_arithmetic(other,{Rational,int},'*','Rational',type_as_str(other))
        if type_as_str(other) == "int":
            other = Rational(other, 1)
        return Rational(self.num*other.num,  self.denom * other.denom)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        self._validate_arithmetic(other,{Rational,int},'/','Rational',type_as_str(other))
        if type_as_str(other) == "int":
            other = Rational(other, 1)
        return Rational(self.num*other.denom,  self.denom * other.num)

    def __rtruediv__(self, other):
        self._validate_arithmetic(other,{Rational,int},'/','Rational',type_as_str(other))
        if type_as_str(other) == "int":
            other = Rational(other, 1)
        return Rational( self.denom * other.num, self.num*other.denom)

    def __pow__(self, other):
        self._validate_arithmetic(other,{int},'**','Rational',type_as_str(other))
        if other == 0:
            return Rational(1,1)
        elif other > 0:
            return Rational(self.num, self.denom**other)
        else:
            return Rational(self.denom, self.num**abs(other))

    def __lt__(self, other):
        self._validate_relational(other,{Rational,int},'<',type_as_str(other))
        if type_as_str(other) == "int":
            other = Rational(other, 1)
        return self.num*other.denom < self.denom*other.num

    def __le__(self, other):
        self._validate_relational(other,{Rational,int},'<=',type_as_str(other))
        if type_as_str(other) == "int":
            other = Rational(other, 1)
        return self.num*other.denom <= self.denom*other.num

    def __eq__(self, other):
        self._validate_relational(other,{Rational,int},'=',type_as_str(other))
        if type_as_str(other) == "int":
            other = Rational(other, 1)
        return self.num*other.denom == self.denom*other.num

    def __ne__(self, other):
        self._validate_relational(other,{Rational,int},'!=',type_as_str(other))
        if type_as_str(other) == "int":
            other = Rational(other, 1)
        return self.num*other.denom != self.denom*other.num

    def __gt__(self, other):
        self._validate_relational(other,{Rational,int},'>',type_as_str(other))
        if type_as_str(other) == "int":
            other = Rational(other, 1)
        return self.num*other.denom > self.denom*other.num

    def __ge__(self, other):
        self._validate_relational(other,{Rational,int},'>=',type_as_str(other))
        if type_as_str(other) == "int":
            other = Rational(other, 1)
        return self.num*other.denom >= self.denom*other.num


    def __bool__(self):
        if self.num == 0:
            return False
        else:
            return True

    def __getitem__(self, index):
        if index == 0:
            return self.num
        elif index == 1:
            return self.denom
        elif type_as_str(index) == "str":
            index = index.lower()
            if "numerator".startswith(index):
                return self.num
            elif "denominator".startswith(index):
                return self.denom
            else:
                raise TypeError()
        else:
            raise TypeError("")

    def __neg__(self):
        return Rational(-self.num, self.denom)

    def __pos__(self):
        return Rational(self.num, self.denom)

    def __abs__(self):
        return Rational(abs(self.num), self.denom)

    def __call__(self, precision):
        fmt = "%%0.%df" % precision
        return fmt % (self.num*1.0/self.denom)

    def __setattr__(self, attr, value):
        calling = inspect.stack()[1]
        if calling.function == "__init__":
            self.__dict__[attr] = value
        else:
            if attr ==  "num":
                raise NameError()
            elif attr == "denom":
                raise NameError()
            else:
                raise NameError()

    @staticmethod
    # Called as Rational._gcd(...); no self parameter
    # Helper method computes the Greatest Common Divisor of x and y
    def _gcd(x : int, y : int) -> int:
        assert type(x) is int and type(y) is int and x >= 0 and y >= 0,\
          'Rational._gcd: x('+str(x)+') and y('+str(y)+') must be integers >= 0'
        while y != 0:
            x, y = y, x % y
        return x
    
    @staticmethod
    # Called as Rational._validate_arithmetic(..); no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), lt (left type) and rt (right type)
    # An example call (from my __add__ method), which checks whether the type of
    #   right is a Rational or int is...
    # Rational._validate_arithmetic(right, {Rational,int},'+','Rational',type_as_str(right))
    def _validate_arithmetic(v : object, t : {type}, op : str, left_type : str, right_type : str):
        if type(v) not in t:
            raise TypeError('unsupported operand type(s) for '+op+
                            ': \''+left_type+'\' and \''+right_type+'\'')        

    @staticmethod
    # Called as Rational._validate_relational(..); no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), and rt (right type)
    def _validate_relational(v : object, t : {type}, op : str, right_type : str):
        if type(v) not in t:
            raise TypeError('unorderable types: '+
                            'Rational() '+op+' '+right_type+'()') 
                   

   # Put all other methods here





# e ~ 1/0! + 1/1! + 1/2! + 1/3! ... 1/n!
def compute_e(n):
    answer = Rational(1)
    for i in irange(1,n):
        answer += Rational(1,math.factorial(i))
    return answer

# Newton: pi = 6*arcsin(1/2); see the arcsin series at http://mathforum.org/library/drmath/view/54137.html
# Check your results at http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html
#   also see http://www.numberworld.org/misc_runs/pi-5t/details.html
def compute_pi(n):
    def prod(r):
        answer = 1
        for i in r:
            answer *= i
        return answer
    
    answer = Rational(1,2)
    x      = Rational(1,2)
    for i in irange(1,n):
        big = 2*i+1
        answer += Rational(prod(range(1,big,2)),prod(range(2,big,2)))*x**big/big       
    return 6*answer


if __name__ == '__main__':
    #Simple tests before running driver

    x = Rational(8,29) 
    print(x+x)
    print(2*x)
    print(x(30))
    print(Rational(1,-2))
    print()
    import driver    
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
