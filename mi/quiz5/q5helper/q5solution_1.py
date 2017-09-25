from functools import reduce # For problem 6
from goody import type_as_str
#
def compare(s1 : str, s2 : str) -> bool:
    if len(s1) == 0:
        if len(s2) ==0:
            return "="
        else:
            return "<"
    else:
        if len(s2) == 0:
            return ">"
        else:
            char1 = s1[0]
            char2 = s2[0]
            if char1 == char2:
                return compare(s1[1:], s2[1:])
            elif char1 < char2:
                return "<"
            else:
                return ">"
            
    
def is_palindrome(s : str) -> bool:
    if len(s) == 1:
        return True
    else:
        if s[0].lower() != s[-1].lower():
            return False
        else:
            return is_palindrome(s[1:-1])



def separate(p : callable, l : [object]) -> ([object],[object]):
    if len(l) == 0:
        return ([], [])
    else:
        if p(l[0]):
            return (separate(p, l[1:])[0] + [l[0]], separate(p, l[1:])[1])
        else:
            return (separate(p, l[1:])[0], separate(p, l[1:])[1] + [l[0]])


def sort(l : [object]) -> [object]:
    # 这里使用快速排序算法，可以参考http://www.cnblogs.com/scorpioying/archive/2012/09/07/2675327.html
    if len(l) == 0:
        return l
    else:
        first = l[0]
        remain = l[1:]
        lt_part = []
        gt_part = []
        for elem in remain:
            if elem > first:
                gt_part.append(elem)
            else:
                lt_part.append(elem)
        return sort(lt_part) + [first] + sort(gt_part)


def unnested(l : 'a nested list') -> [object]:
    if len(l) == 0:
        return l
    else:
        first = l[0]
        if type_as_str(first) != "list":
            return [first] + unnested(l[1:])
        else:
            return unnested(first) + unnested(l[1:])


def merge(x : [str], y : str) -> [str]:
    if len(x) == 0:
        return [y]
    else:
        if len(x[0]) < len(y):
            return [y]
        elif len(x[0]) == len(y):
            return x + [y]
        else:
            return x
        
def all_longest(file : open) -> [str]:
    lines = [line.strip() for line in file]
    f = filter(lambda line:line[0]!="#", lines)
    r = reduce(merge, list(f), [])
    return r

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
    
