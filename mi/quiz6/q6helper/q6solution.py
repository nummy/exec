import prompt
from functools import reduce


# List Node class and helper functions (to set up problem)

class LN:
    def __init__(self,value,next=None):
        self.value = value
        self.next  = next

def list_to_ll(l):
    if l == []:
        return None
    front = rear = LN(l[0])
    for v in l[1:]:
        rear.next = LN(v)
        rear = rear.next
    return front

def str_ll(ll):
    answer = ''
    while ll != None:
        answer += str(ll.value)+'->'
        ll = ll.next
    return answer + 'None'



# Tree Node class and helper functions (to set up problem)

class TN:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left  = left
        self.right = right

def list_to_tree(alist):
    if alist == None:
        return None
    else:
        return TN(alist[0],list_to_tree(alist[1]),list_to_tree(alist[2])) 
    
def str_tree(atree,indent_char ='.',indent_delta=2):
    def str_tree_1(indent,atree):
        if atree == None:
            return ''
        else:
            answer = ''
            answer += str_tree_1(indent+indent_delta,atree.right)
            answer += indent*indent_char+str(atree.value)+'\n'
            answer += str_tree_1(indent+indent_delta,atree.left)
            return answer
    return str_tree_1(0,atree) 



# Define pair_sum ITERATIVELY

def no_adj_dup(ll):
    if ll is None:
        return None
    front = rear = LN(ll.value)
    while ll != None:
        value = ll.value
        ll = ll.next
        if value != rear.value:
            rear.next = LN(value)
            rear = rear.next
    return front
            


# Define pair_sum_r RECURSIVELY
def no_adj_dup_r(ll):
    # ll is None or have only on node
    if ll is None or ll.next is None:
        return ll
    # init nodes
    front = rear = LN(ll.value)
    # if next node's value == last node's value, jump to next node
    if ll.next.value == rear.value:
        ll = ll.next.next
    else:
        ll = ll.next
    result = no_adj_dup_r(ll)
    # if recursive result's first node.value = rear.value redo with next node
    if result and result.value == rear.value:
        result = no_adj_dup_r(ll.next)
    rear.next = result
    rear = rear.next
    return front



# Define bases RECURSIVELY
def bases(aclass):
    parents = set(aclass.__bases__)
    # get all bases recursively
    arr = [bases(parent) for parent in parents]
    # union all set
    result=reduce(lambda x,y:x|y, arr, set())
    # return final result
    return result.union(parents)


# Define the derived StingVar_WithHistory using the StringVar base class defined in tkinter

from tkinter import StringVar

class StringVar_WithHistory(StringVar):
    def __init__(self):
        super(StringVar_WithHistory, self).__init__()
        self.history = []

    def set(self, value):
        if self.get() != value:
            self.history.append(value)
            super(StringVar_WithHistory, self).set(value)

    def undo(self):
        if len(self.history) == 1:
            pass
        else:
            self.history.pop()
            value = self.history[-1]
            super(StringVar_WithHistory, self).set(value)




            
# OptionMenuUndo: acts like an OptionMenu, but also allows undoing the most recently
#   selected option, all the way back to the title (whose selection cannot be undone).
# It overrides the __init__ method and defines the new methods get, undo, and 
#   simulate_selections.
# It will work correctly if StringVar_WithHistory is defined correctly
from tkinter import OptionMenu
class OptionMenuUndo(OptionMenu):
    def __init__(self,parent,title,*option_tuple,**configs):
        self.result = StringVar_WithHistory()
        self.result.set(title)
        OptionMenu.__init__(self,parent,self.result,*option_tuple,**configs)

    # Get the current option  
    def get(self):                
        return self.result.get() # Call get on the StringVar_WithHistory attribute

    # Undo the most recent option
    def undo(self):
        self.result.undo()       # Call undo on the StringVar_WithHistory attribute
      
    # Simulate selecting an option (mostly for test purposes)
    def simulate_selection(self,option):
        self.result.set(option)  # Call set on the StringVar_WithHistory attribute


# Testing Script

if __name__ == '__main__':
    print('Testing no_adj_dup')
    ll = list_to_ll([])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1,1])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup(ll)))
    print('original list is now       = ',str_ll(ll))

    ll = list_to_ll([1,2])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1,1,2])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1,2,2])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1,1,1,2,2,3,3,3,4,4,5,5,5])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1,2,3,4,5])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1,1,2,2,2,3,4,3,3,5,5,6,7,7])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup(ll)))
    print('original list is now       = ',str_ll(ll))
    
    
    # Put in your own tests here


    print('\nTesting no_adj_dup_r')
    ll = list_to_ll([])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup_r(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup_r(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1,1])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup_r(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1,2])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup_r(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1,1,2])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup_r(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1,2,2])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup_r(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1,1,1,2,2,3,3,3,4,4,5,5,5])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup_r(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1,2,3,4,5])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup_r(ll)))
    print('original list is now       = ',str_ll(ll))
    
    ll = list_to_ll([1,1,2,2,2,3,4,3,3,5,5,6,7,7])
    print('\noriginal list              = ',str_ll(ll))
    print('resulting list             = ',str_ll(no_adj_dup_r(ll)))
    print('original list is now       = ',str_ll(ll))

    # Put in your own tests here


    print('\nTesting bases')
    
    class F:pass
    class C:pass
    class G:pass
    class B(F):pass
    class D(G):pass
    class A(B,C,D):pass
    print(bases(A))
    
    class A          : pass    
    class B          : pass
    class C(A)       : pass    
    class D(A,B)     : pass
    class E(A)       : pass
    class F(C,D)     : pass    
    class G(B)       : pass
    class H(E,F,G)   : pass
    print(bases(H))
          
    # Put in your own tests here
          
  

    print('\nTesting OptionMenuUndo')
    from tkinter import *
    print('Simulate using StringVar_WithHistory or build/test actual GUI')
    if prompt.for_bool('Simulate',default=True):
        # Needed for obscure reasons: OptionMenu must still be placed in main
        root = Tk()
        root.title('Widget Tester')
        main = Frame(root)
        
        # Construct an OptionMenuUndo object for simulation
        omu = OptionMenuUndo(main, 'Choose Option', 'option1','option2','option3')
        
        # Initially its value is 'Choose Option'
        print(omu.get(), '   should be Choose Option')
        
        # Select a new option
        omu.simulate_selection('option1')
        print(omu.get(), '         should be option1')
        
        # Select a new option
        omu.simulate_selection('option2')
        print(omu.get(), '         should be option2')
        
        # Select the same option (does nothing)
        omu.simulate_selection('option2')
        print(omu.get(), '         should still be option2')
        
        # Select a new option
        omu.simulate_selection('option3')
        print(omu.get(), '         should be option3')
         
        # Undo the last option: from 'option3' -> 'option2'
        omu.undo()
        print(omu.get(), '         should go back to option2')
         
        # Undo the last option: from 'option2' -> 'option1'
        omu.undo()
        print(omu.get(), '         should go back to option1')
         
        # Undo the last option: from 'option1' -> 'Choose Option'
        omu.undo()
        print(omu.get(), '   should go back to Choose Option')
         
        # Cannot undo the first option: does nothing
        omu.undo()
        print(omu.get(), '   should still be Choose Option')

         
        # Cannot undo the first option: does nothing
        omu.undo()
        print(omu.get(), '   should still be Choose Option')
        
    else: #Build/Test real widget

        # #OptionMenuToEntry: with title, linked_entry, and option_tuple
        # #get is an inherited pull function; put is a push function, pushing
        # #  the selected option into the linked_entry (replacing what is there)
        # 
        root = Tk()
        root.title('Widget Tester')
        main = Frame(root)
        main.pack(side=TOP,anchor=W)
         
        omu = OptionMenuUndo(main, 'Choose Option', 'option1','option2','option3')
        omu.grid(row=1,column=1)
        omu.config(width = 10)
         
        b = Button(main,text='Undo Option',command=omu.undo)
        b.grid(row=1,column=2)
         
        root.mainloop()    
