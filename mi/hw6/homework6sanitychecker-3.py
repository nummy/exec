from vertex import Vertex
from homework6 import *

def print_if_error(description:str, result, expected)->None:
    if not (expected == result):
        print(description)
        print("Expected:   ", expected)
        print("Result:     ", result)     

def test_fibonacci():
    expected = [1, 1, 2, 3, 5, 8, 13, 21]
    f = fibonacci()
    result = []
    for i in range(len(expected)):
        result.append(next(f))
    print_if_error("fibonacci incorrect", result, expected)

def example_undirected()->Graph:
    vertices = list(range(1,14))
    g1 = Graph(vertices, [(1, 3), (2, 3), (3, 4), (3, 5), 
                            (6, 7), (6, 8), (7, 8)])
    g1.add_edge(9, 10)
    g1.add_edge(10, 11)
    g1.add_edge(11, 12)
    g1.add_edge(12, 13)
    #see picture of given test graph
    return g1

def test_graph():
    g = example_undirected()
    expected = list(reversed(range(1,14)))
    result = []
    it = iter(g)
    for i in range(len(expected)):
        result.append(next(it))
    print_if_error("graph with iter incorrect", result, expected)
    
    result = []
    for v in g:
        result.append(v)
    print_if_error("graph with for loop incorrect", expected, result)

def test_connected_vertices():
    expected = list(reversed(range(1,14)))
    result = []
    for v in ConnectedVertices(example_undirected()):
        result.append(v)
    print_if_error("connected vertices with for loop incorrect", result, expected)
    
def test_components():
    expected = [9, 6, 1]
    result = []
    for v in Components(example_undirected()):
        result.append(v)
    print_if_error("components with for loop incorrect", result, expected)

def test_prime():
    it = get_first_n_digit_prime(5)
    expected = [2, 11, 101, 1009, 10007]
    result = []
    try:
        for i in range(len(expected) + 1):
            result.append(next(it))
    except StopIteration:
        print_if_error("get_first_n_digit_prime incorrect", result, expected)
    else:
        print("failed to raise StopIteration")
    
if __name__ == "__main__":
    test_fibonacci()
    test_graph()
    test_connected_vertices()
    test_components()
    test_prime()
