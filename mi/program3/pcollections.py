import re, traceback, keyword, goody
import inspect


def pnamedtuple(type_name, field_names, mutable=False):
    class_definition='''\
import goody
import inspect

class {type_name}:
    # __init__ function 
    {init}

    def __repr__(self):
        return "{type_name}(%s)" % (",".join([field + '=' + str(self[field]) for field in self._fields]))

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

    # get function, example:get_x, get_y, get_z
    {get_func}
    def __eq__(self, other):
        # eq function 
        print(goody.type_as_str(other))
        if goody.type_as_str(other) != 'pnamedtuple_{type_name}.{type_name}':
            return False
        if len(self._fields) != len(other._fields):
            return False
        for field in self._fields:
            if self[field] != other[field]:
                return False
        return True

    def _replace(self, **kargs):
        for k, v in kargs.items():
            if k not in self._fields:
                raise TypeError("%s is not exist" % k)
        if self._mutable:
            for k, w in kargs.items():
                if k in self._fields:
                    self.__dict__[k] = v
            return None
        else:
            temp = dict()
            for field in self._fields:
                temp[field] = self[field]
                if field in kargs:
                    temp[field] = kargs[field]
            return {type_name}(**temp)

    def __setattr__(self, key, value):
        calling = inspect.stack()[1]
        if calling.function == "__init__":
            self.__dict__[key] = value
        else:
            if self._mutable:
                self.__dict__[key] = value
            else:
                raise AttributeError("the pnamedtuple it not mutable")
'''
    def show_listing(s):
        for l,t in enumerate(s.split('\n'), 1):
            print('{line: >4} {text}'.format(line = l, text = t.rstrip()))

    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    # check valid name 
    pattern = re.compile(r'^[a-zA-Z]\w*$')
    kwlist = keyword.kwlist
    type_name = str(type_name).strip()
    if not pattern.match(type_name) or type_name in kwlist:
        raise SyntaxError("Type name %s is illegal" % type_name)

    fields = []
    if goody.type_as_str(field_names) == "str":
        field_names = field_names.strip()
        fields = re.split(r";|,|\s+", field_names)
    elif goody.type_as_str(field_names) == "list":
        fields = field_names
    else:
        raise SyntaxError("Field names %s are illegal" % str(field_names))

    # remove duplicated field
    unique = []
    for field in fields:
        field = field.strip()
        if field not in unique and field is not "":
            unique.append(field)
    fields = unique
    for field in fields:
        if not pattern.match(field) or field in kwlist:
            raise SyntaxError("Field name %s is illegal" % field)

    def gen_init(fields):
        init_template = "def __init__(self, {}):\n".format(",".join(fields))
        for field in fields:
            init_template += "        self.{} = {}\n".format(field, field)
        init_template += "        self._fields = {}\n".format('['+','.join(["'" + i + "'" for i in fields]) + ']')
        init_template += "        self._mutable = {}".format(str(mutable))
        return init_template

    def gen_get(fields):
        get_template = ""
        for field in fields:
            temp = "\n    def get_{field}(self):\n        return self.{field}\n".format(field=field)
            get_template += temp
        return get_template

    init_template = gen_init(fields)
    get_template = gen_get(fields)
    #class_definition = open("class.txt", "r").read()
    class_definition = class_definition.format(type_name=type_name, init=init_template, get_func=get_template)

    # For initial debugging, always show the source code of the class
    #show_listing(class_definition)
    # Execute the class_definition string in a local namespace; then, bind the
    #   name source_code in its dictionary to the class_defintion; return the
    #   class object created; if there is a syntax error, list the class and
    #   also show the error
    name_space = dict(__name__='pnamedtuple_{type}'.format(type = type_name))
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except(TypeError, SyntaxError):
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test pnamedtuple below: e.g., Point = pnamedtuple('Point', 'x y')
    import driver
    driver.driver()