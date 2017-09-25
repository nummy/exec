from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation():
    # set the class attribute below to True for checking to occur
    checking_on  = True
  
    # self._checking_on must also be true for checking to occur
    def __init__(self, f):
        self._f = f
        self._checking_on = True
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters. 
    # here I add param_args, because in function check_str, it needs all the params as locals in eval()
    def check(self,param,annot,value,check_history='', param_args=None):  
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)
        def check_list(param, annot, value, check_history):
            # value's type is list
            assert isinstance(value, list), repr(param)+' failed annotation check_list(): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history      
            if len(annot) ==  1:            # element in the list must be the same type
                for v in value:
                    # recursive check their type
                    self.check(param, annot[0], v, check_history)   
            else:
                # length must be the same
                assert len(annot) == len(value), repr(param)+' failed annotation check_list(): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history   
                for index, v in enumerate(value):
                    # recursive check their type
                    self.check(param, annot[index],v, check_history)

        def check_tuple(param, annot, value, check_history):
            # value's type is tuple
            assert isinstance(value, tuple),repr(param)+' failed annotation check_tuple(): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history   
            # element in the tuple are the same type
            if len(annot) ==  1:
                for v in value:
                    # recursive check their type
                    self.check(param, annot[0], v, check_history)
            else:
                # length of annot and value must be the same
                assert len(annot) == len(value), repr(param)+' failed annotation check_tuple(): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history   
                for index, v in enumerate(value):
                    # recursive check their their type
                    self.check(param, annot[index], v, check_history)

        def check_dict(param, annot, value, check_history):
            # if value's type if dict
            assert isinstance(value, dict), repr(param)+' failed annotation check_dict(): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history  
            assert len(annot)==1            # length of annot must be 1
            if len(annot) == 1:             
                key_type = list(annot.keys())[0]        # get the type of k
                value_type = list(annot.values())[0]    # get the type of v
                for k, v in value.items():
                    # check whether their type are the same, use recursion
                    self.check(param, key_type, k, check_history)
                    self.check(param, value_type, v, check_history)

        def check_set(param, annot, value, check_history):
            # if value's type is set
            assert isinstance(value, set), repr(param)+' failed annotation check_set(): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history  
            assert len(annot)==1    # len(annot) must  be 1
            if len(annot) == 1:
                # get the type of element
                value_type = annot.pop()
                for v in value:
                    # check whether their type are the same
                    self.check(param, value_type, v, check_history)

        def check_frozenset(param, annot, value, check_history):
            # if value is instanceof frozenset
            assert isinstance(value, frozenset),repr(param)+' failed annotation check_frozenset(): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history  
            assert len(annot)==1    # annot has only one element
            if len(annot) == 1:
                value_type = list(annot)[0] # get type of the element 
                for v in value:
                    # check whether their type are the same
                    self.check(param, value_type, v, check_history)

        def check_lambda(param, annot, value, check_history):
            # if the length os varnames=1
            assert len(annot.__code__.co_varnames)==1
            try:
                # get the result of function
                result = annot(value)
            except:
                raise AssertionError("lambda function failed")
            assert result is True

        def check_obj(param, value, check_history):
            try:
                # call __check__annotation__
                value.__check_annotation__(self.check, param, value, check_history)
            except AttributeError as e:
                raise AssertionError("object does not have method __check_annotation__")
            except:
                raise AssertionError("check failed")


        def check_str(param, annot, value, check_history, param_args):
            try:
                # evalutaion the annot, with locals=param_args
                # eval('code', locals={})
                result = eval(annot,dict(param_args))
            except:
                raise AssertionError("eval failed")
            assert result is True

        # Decode your annotation next; then check against argument
        if annot is None:
            pass
        elif isinstance(annot, type):
            assert isinstance(value, annot), "failed annotation check"
        elif isinstance(annot, list):
            check_list(param, annot, value, check_history)
        elif isinstance(annot, tuple):
            check_tuple(param, annot, value, check_history)
        elif isinstance(annot, dict):
            check_dict(param, annot, value, check_history)
        elif isinstance(annot, set):
            check_set(param, annot, value, check_history)
        elif isinstance(annot, frozenset):
            check_frozenset(param, annot, value, check_history)
        elif inspect.isfunction(annot):
            check_lambda(param, annot, value, check_history)
        elif isinstance(annot, str):
            check_str(param, annot, value, check_history, param_args)
        else:
            check_obj(param, value, check_history)


    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict: the order parameters appear in the function's header)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name  not in  bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        
        try:
            if self._checking_on and self._f:
                # get annotations
                annotations = self._f.__annotations__
                # get params and args 
                param_args = param_arg_bindings()
                check_history = ''
                return_annot =  None
                # if function has return annotation
                if "return" in annotations:
                    return_annot = annotations["return"]
                for param, annot in annotations.items():
                    if param == "return":
                        pass
                    else:
                        # traverse params and args, check the annotations
                        value = param_args.get(param)
                        self.check(param, annot, value, check_history, param_args=param_args)
                result = self._f(*args, **kargs)
                if return_annot:
                    # function have return annotation
                    self.check("_return", return_annot, result, check_history)
                return result
            else:
                return None
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
            # print(80*'-')
            # for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
            #     print(l.rstrip())
            # print(80*'-')
            raise


  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
    def f(x:int): pass
    f = Check_Annotation(f)
    f(2)

    import driver
    driver.driver()
