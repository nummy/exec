from functools import reduce # For problem 6
from goody import type_as_str

def compare(s1 : str, s2 : str) -> bool:
    if len(s1) == 0  and len(s2) ==0:
        return "="
    if len(s1) == 0 and len(s2) != 0:
        return "<"
    if len(s2) == 0 and len(s1) != 0:
        return ">"
    if len(s1) != 0 and len(s2) != 0:
        c1 = s1[0]
        c2 = s2[0]
        if c1 == c2:
            return compare(s1[1:], s2[1:])
        elif c1 < c2:
            return "<"
        else:
            return ">"
            
    
def is_palindrome(s : str) -> bool:
    if len(s) == 1:
        return True
    start = s[0].lower()
    end = s[-1].lower()
    if start != end:
        return False
    else:
        remain = s[1:-1]
        return is_palindrome(remain)



def separate(p : callable, l : [object]) -> ([object],[object]):
    if len(l) == 0:
        return ([], [])
    remain = separate(p, l[1:])
    if not p(l[0]):
        return (remain[0], remain[1] + [l[0]])
    else:
        return (remain[0] + [l[0]], remain[1])


def sort(l : [object]) -> [object]:
    if len(l) == 0:
        return []
    pivot = l[0]
    other = l[1:]
    left = []
    right = []
    for elem in other:
        if elem <= pivot:
            left.append(elem)
        else:
            right.append(elem)
    return sort(left) + [pivot] + sort(right)


def unnested(l : 'a nested list') -> [object]:
    if len(l) == 0:
        return l
    f = l[0]
    remain = unnested(l[1:])
    if type_as_str(f) != "list":
        return [f] + remain
    else:
        return unnested(f) + remain


def merge(x : [str], y : str) -> [str]:
    if len(x) == 0:
        return [y]
    len_x = len(x[0])
    len_y = len(y)
    if len_x < len_y:
        return [y]
    elif len_x > len_y:
        return x
    else:
        return x + [y]
        
def all_longest(file : open) -> [str]:
    return reduce(merge, filter(lambda x:x[0]!="#", map(lambda x:x.strip(), file)))

if __name__=="__main__":
    import predicate,random,driver
    from goody import irange
    
    print('Testing compare')
    print('',      compare('',''),          '')
    print('',      compare('','abc'),       'abc')
    print('abc',   compare('abc',''),       '')
    print('abc',   compare('abc','abc'),    'abc')
    print('bc',    compare('bc','abc'),     'abc')
    print('abc',   compare('abc','bc'),     'bc')
    print('aaaxc', compare('aaaxc','aaabc'), 'aaabc')
    print('aaabc', compare('aaabc','aaaxc'), 'aaaxc')
   
    print('\nTesting is_palindrome')
    print('DoGeeseSeeGod',          is_palindrome('DoGeeseSeeGod'))
    print('AbleWasIEreISawElba',    is_palindrome('AbleWasIEreISawElba'))
    print('AManAPlanACanalPanama',  is_palindrome('AManAPlanACanalPanama'))
    print('DoGeesesSeeGod',         is_palindrome('DoGeesesSeeGod'))
    print('AbleIWasEhenISawElba',   is_palindrome('AbleIWasEhenISawElba'))
    print('AManAPlaneACanalPanama', is_palindrome('AManAPlaneACanalPanama'))
    
    print('\nTesting separate')
    print(separate(predicate.is_positive,[]))
    print(separate(predicate.is_positive,[1, -3, -2, 4, 0, -1, 8]))
    print(separate(predicate.is_prime,[i for i in irange(2,20)]))
    print(separate(lambda x : len(x) <= 3,'to be or not to be that is the question'.split(' ')))
    print(separate(lambda x : x <= 'm','to be or not to be that is the question'.split(' ')))
     
    print('\nTesting sort')
    print(sort([1,2,3,4,5,6,7]))
    print(sort([7,6,5,4,3,2,1]))
    print(sort([4,5,3,1,2,7,6]))
    print(sort([1,7,2,6,3,5,4]))
    l = [i+1 for i in range(30)]
    random.shuffle(l)
    print(l)
    print(sort(l))
    
    print('\nTesting nested_count')
    print(unnested([1,2,4,1,8,1,3,2,1,1]))
    print(unnested([[1,2,4,1,8],[1,3,2],1,1]))
    print(unnested([[1,2,[4,[1],8],[1,3,2]],[1,1]]))

    print('\nTesting merge')
    print(merge([],'abc'))
    print(merge(['abc', 'lmn'],'wxyz'))
    print(merge(['abc', 'lmn'],'xyz'))
    print(merge(['abc', 'lmn'],'xy'))
    
    print('\nTesting all_longest')
    for l in all_longest(open('test1.txt')):
        print(l)
    print()

    driver.default_file_name = 'bsc.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
    
