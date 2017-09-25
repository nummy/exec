#see helpers.py for imported code

import prompt
from helpers import primes, hide


def differences(iterable1,iterable2):
    zipped_list = zip(iterable1, iterable2)
    for index, data in enumerate(zipped_list):
        if data[0] != data[1]:
            yield (index+1, data[0], data[1])
   
def once_in_a_row(iterable):
    last = None
    for index, elem in enumerate(iterable):
        if index == 0:
            last = elem
            yield elem
        else:
            if elem == last:
                last = elem
                continue
            else:
                last = elem
                yield elem


def in_between(iterable, starter, stopper):
    # 123abczdefalmanozstuzavuwz45z
    # abczalmanozzavuwzz
    flag = False
    for index, elem in enumerate(iterable):
        if starter(elem):
            flag = True
            yield elem
        elif stopper(elem):
            if flag:
                yield elem
            flag = False
        else:
            if flag:
                yield elem



def group(iterable,n):
    temp = iter(iterable)
    while True:
        res = []
        flag = False
        try:
            for i in range(n):
                res.append(next(temp))
        except:
            pass
            flag = True
        finally:
            if not flag:
                yield res
        if flag:
            break


def slice_gen(iterable, start, stop, step):
    assert (start >= 0) is True
    assert (stop >= 0) is True
    assert(step>0) is True
    temp = iter(iterable)
    count = 0
    while True:
        try:
            elem = next(temp)
            if count == start:
                if start < stop:
                    start = start + step
                    yield elem
                else:
                    break
            count += 1
        except StopIteration as e:
            break
        
    
def shuffle(*args):
    items = []
    for arg in args:
        items.append(iter(arg))
    while True:
        flags = {}
        for index, item in enumerate(items):
            if index in flags:
                continue
            try:
                temp = next(item)
                yield temp
            except StopIteration:
                flags[index] = True
        if len(flags) == len(args):
            break

        

class Backwardable:
    def __init__(self,iterable):
        self._iterable = iterable
            
    def __iter__(self):
        class B_iter:
            def __init__(self,iterable):
                self._all      = []
                self._iterator = iter(iterable)
                self._index    = -1 # index of just returned value from __next__ or __prev__
        
            def __str__(self):
                return '_all={}, _index={}'.format(self._all,self._index)
        
            def __next__(self):
                if self._index + 1  < len(self._all):
                    elem = self._all[self._index +1]
                else:
                    elem = next(self._iterator)
                    self._all.append(elem)
                self._index += 1
                return elem
                
            def __prev__(self):
                if self._index == 0:
                    raise AssertionError()
                else:
                    elem = self._all[self._index-1]
                    self._index -= 1
                    return elem
            
        return B_iter(self._iterable)



def prev(x): return x.__prev__()


def mini_Backwardable_test(i):
    print('\n\nmini_Backwardable_test: enter sequences of next/prev operations (or quit)')
    while True:
        print('\ni =',i)
        command = prompt.for_char('Enter 1-character Command: [n]ext, [p]rev, or [q]uit', legal= 'npq')
        try:
            if command == 'n':
                print(' ',next(i))
            elif command == 'p':
                print(' ',prev(i))
            else:
                break;
        except:
            print('  command raised exception')


if __name__ == '__main__':
    # Test differences; you can add your own test cases
    print('Testing differences')
    for i in differences('3.14159265', '3x14129285'):
        print(i,end=' ')    
    print()

    for i in differences(hide('3.14159265'), hide('3x14129285')):
        print(i,end=' ')    
    print()

    for i in differences(primes(), hide([2, 3, 1, 7, 11, 1, 17, 19, 1, 29])):
        print(i,end=' ')    
    print('\n')
              
    # Test once_in_a_row; you can add your own test cases
    print('\nTesting once_in_a_row')
    for i in once_in_a_row('abcccaaabddeee'):
        print(i,end='')    
    print()

    for i in once_in_a_row(hide('abcccaaabddeee')):
        print(i,end='')    
    print('\n')
    
        
    # Test in_between; you can add your own test cases
    print('\nTesting in_between')
    for i in in_between('123abczdefalmanozstuzavuwz45z', (lambda x : x == 'a'), (lambda x : x == 'z')):
        print(i,end='')
    print()
    
    for i in in_between(hide('123abczdefalmanozstuzavuwz45z'), (lambda x : x == 'a'), (lambda x : x == 'z')):
        print(i,end='')
    print()

    for i in in_between(primes(), (lambda x : x%10 == 3), (lambda x : x%10 == 7)):
        print(i,end=' ')
        if i > 100:
            break
    print('\n')


    # Test group' you can add your own test cases
    print('\nTesting group')
    for i in group('abcdefghijklm',4):
        print(i,end='')
    print()
    
    for i in group(hide('abcdefghijklm'),4):
        print(i,end='')
    print()

    for i in group(primes(),5):
        print(i,end=' ')
        if i[3] > 100:
            break
    print('\n')


    # Test slice_gen; add your own test cases
    print('\nTesting slice_gen')
    for i in slice_gen('abcdefghijk', 3,7,1):
        print(i,end='')
    print()
       
    for i in slice_gen('abcdefghijk', 3,20,1):
        print(i,end='')
    print()
       
    for i in slice_gen(hide('abcdefghijklmnopqrstuvwxyz'), 3, 20, 3):
        print(i,end='')
    print()
       
    for i in slice_gen(primes(), 100,200,5):
        print(i,end=' ')
    print('\n')

    
    # Test alternate; add your own test cases
    print('\nTesting shuffle')
    for i in shuffle('abcde','fg','hijk'):
        print(i,end='')
    print()
       
    for i in shuffle(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print()
       
    for i in shuffle(primes(), hide('fghi'), hide('jk')):
        print(i,end=' ')
        if type(i) is int and i > 20:
            break; 
    print()



    # Test Backwardable; add your own test cases
    print('\nTesting Backwardable')
    s = 'abcde'
    i = iter(Backwardable(s))
    print(i)
    print(next(i),i) #a
    print(next(i),i) #b
    print(next(i),i) #c
    print(prev(i),i) #b
    print(prev(i),i) #a
    try:
        print(prev(i),i)
    except AssertionError:
        print('Tried to prev before first value')
    print(next(i),i) #b
    print(next(i),i) #c
    print(next(i),i) #d
    print(next(i),i) #e
    try:
        print(next(i),i)
    except StopIteration:
        print('Correctly raised StopIteration')

    # See the mini_Backwardable_test code, which allows you to call
    #  interleaved sequences of next and prev, or quit
    mini_Backwardable_test(iter(Backwardable('abc')))
    mini_Backwardable_test(iter(Backwardable([0,1,2,3,4])))
    mini_Backwardable_test(iter(Backwardable(primes())))
    
    
    import driver
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
