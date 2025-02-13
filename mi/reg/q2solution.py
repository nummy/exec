import re
from goody import irange
from collections import defaultdict

# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1a.txt, repattern1b.txt, and
#   repattern2a.txt. The patterns must be all on the first line


def pages (page_spec, unique):
    raws = page_spec.split(",")
    pattern = r"^([1-9]\d*)(:|-)?([1-9]\d*)?/?([1-9]\d*)?$"
    res = []
    for raw in raws:
        m = re.match(pattern, raw)
        assert m is not None 
        (start, sep, end, step) = m.groups()
        if sep is None:
            start = int(start)
            res.append(start)
        elif sep is ":":
            start = int(start)
            end = int(end)
            if step is None:
                res.extend(list(range(start, start+end)))
            else:
                step = int(step)
                res.extend(list(range(start, end*step+start, step)))
                pass
        elif sep is "-":
            start = int(start)
            end = int(end)
            assert start <= end
            if step is None:
                res.extend(list(range(start, end+1)))
            else:
                step = int(step)
                res.extend(list(range(start, end+1, step)))
    if unique:
        res=list(set(res))        
        res.sort()
        return res
    else:
        res.sort()
        return res


def expand_re(pat_dict):
    keys = pat_dict.keys()
    for key1 in keys:
        pat = re.compile(r"#"+key1+"#")
        sub = pat_dict.get(key1,"")
        sub = re.sub("\\{1}", "", sub)
        sub = "(?:" + sub + ")"
        for key2 in keys:
            if key1 is not key2:
                val = pat_dict.get(key2,"")
                val = re.sub(pat, sub, val)
                pat_dict[key2]=val


if __name__ == '__main__':
    
    p1a = open('repattern1a.txt').read().rstrip() # Read pattern on first line
    print('Testing the pattern p1a: ',p1a)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1a,text)
        print(' ','Matched' if m != None else "Not matched")
        
    p1b = open('repattern1b.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p1b: ',p1b)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1b,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
        
    p2 = open('repattern2a.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p2: ',p2)
    for text in open('bm2a.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p2,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
    print('\nTesting pages function')
    for text in open('bm2b.txt'):
        text = text.rstrip().split(';')
        text,unique = text[0], text[1]=='True'
        try:
            p = pages(text,unique)
            print('  ','pages('+text+','+str(unique)+') = ',p)
        except Exception as e:
            print(e)
            print('  ','pages('+text+','+str(unique)+') = raised exception')
        
    
    print('\nTesting expand_re')
    pd = dict(digit=r'\d', integer=r'[=-]?#digit##digit#*')
    print('  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary
    # {'digit': '\\d', 'integer': '[=-]?(?:\\d)(?:\\d)*'}
    
    pd = dict(integer       = r'[+-]?\d+',
              integer_range = r'#integer#(..#integer#)?',
              integer_list  = r'#integer_range#(?,#integer_range#)*',
              integer_set   = r'{#integer_list#?}')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer':       '[+-]?\\d+',
    #  'integer_range': '(?:[+-]?\\d+)(..(?:[+-]?\\d+))?',
    #  'integer_list':  '(?:(?:[+-]?\\d+)(..(?:[+-]?\\d+))?)(?,(?:(?:[+-]?\\d+)(..(?:[+-]?\\d+))?))*',
    #  'integer_set':    '{(?:(?:(?:[+-]?\\d+)(..(?:[+-]?\\d+))?)(?,(?:(?:[+-]?\\d+)(..(?:[+-]?\\d+))?))*)?}'
    # }
    
    pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'a': 'correct',
    #  'b': '(?:correct)',
    #  'c': '(?:(?:correct))',
    #  'd': '(?:(?:(?:correct)))',
    #  'e': '(?:(?:(?:(?:correct))))',
    #  'f': '(?:(?:(?:(?:(?:correct)))))',
    #  'g': '(?:(?:(?:(?:(?:(?:correct))))))'
    # }
    
    print()
    print()
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
