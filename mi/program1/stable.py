import prompt
import goody
import copy
from collections import defaultdict

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    match_preferences = defaultdict(list)
    for line in open_file:
        arr = line.strip().split(";")
        match_preferences[arr[0]].append(None)
        match_preferences[arr[0]].append(arr[1:])
    return match_preferences


def dict_as_str(d : {str:[str,[str]]}, key: callable=None, reverse : bool=False) -> str:
    res = ""
    for k in sorted(d, key=key, reverse=reverse):
        res =  res + "  %s -> %s\n" % (k, repr(d[k]))
    return res


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    return p1 if order.index(p1) < order.index(p2) else p2


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    res = set()
    for man, match in men.items():
        res.add((man, match[0]))
    return res



def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    pass    
  


  
    
if __name__ == '__main__':
    # Write script here
    # m_file = goody.safe_open('Enter a file representing men   preferences','r','Illegal file name')
    # w_file = goody.safe_open('Enter a file representing women preferences','r','Illegal file name')
    # match_preferences = read_match_preferences(m_file)
    # print(dict_as_str(match_preferences))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
    driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
