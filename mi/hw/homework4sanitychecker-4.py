from vertex import Vertex
from homework4 import Graph

vertices = list(range(1,14))

def print_if_error(description:str, result, expected)->None:
    if not (expected == result):
        print(description)
        print("Expected:   ", expected)
        print("Result:     ", result)        

def create_example_graph():
    g1 = Graph(vertices, [(1, 3), (2, 3), (3, 4), (3, 5), 
                            (6, 7), (6, 8), (7, 8),
                            (9, 10), (10, 11), (11, 12), (12, 13)]) 
    #see picture of given test graph
    return g1

def verify_example_graph(g1:Graph)->None:
    #test degrees
    expected_degrees = [1, 1, 4, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1]
    for vertex_id, expected in list(zip(vertices, expected_degrees)):
        print_if_error("Degree of vertex {}".format(vertex_id), g1.degree(vertex_id), expected)

    #test component size
    print_if_error("Error: component_size() returns different value for these two calls",
            g1.component_size(1), g1.component_size(1)) 
    expected_sizes = [5, 5, 5, 5, 5, 3, 3, 3, 5, 5, 5, 5, 5]
    for vertex_id, expected in list(zip(vertices, expected_sizes)):
        print_if_error("Size of component containing vertex {}".format(vertex_id), 
            g1.component_size(vertex_id), expected)

    #test component count
    expected_components = 3
    print_if_error("Error: count_components() returns different value for these two calls", 
            g1.count_components(), g1.count_components())
    print_if_error("number of components in g1", g1.count_components(), expected_components)

    print_if_error("length of g1 incorrect", len(g1), len(vertices))

    print_if_error("str function incorrect", str(g1), 
                "Graph(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), components=3")

    print_if_error("repr function incorrect", repr(g1), "Graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [(1, 3), (2, 3), (3, 4), (3, 5), (6, 7), (6, 8), (7, 8), (9, 10), (10, 11), (11, 12), (12, 13)])")

def test_equality()->None:    
    g1 = create_example_graph()
    g2 = Graph(vertices, [(1, 3), (2, 3), (3, 4), (3, 5), 
                            (6, 7), (6, 8), #g2 is missing (7, 8) from g1
                            (9, 10), (10, 11), (11, 12), (12, 13)]) 

    g3 = Graph(list(range(1, 15)), [(1, 3), (2, 3), (3, 4), (3, 5), #g3 has an additional vertex
                            (6, 7), (6, 8), (7, 8),
                            (9, 10), (10, 11), (11, 12), (12, 13)]) 

    print_if_error("length of g2 incorrect", len(g2), len(vertices))
    print_if_error("length of g3 incorrect", len(g3), len(list(range(1, 15))))

    #__eq__ test
    print_if_error("g1 should be equal to itself", (g1 == g1), True)
    print_if_error("graphs with different edges are not identical", (g1 == g2), False)
    print_if_error("graphs with different vertices are not identical", (g1 == g3), False)
    try:
        g1 == [1, 2, 3]
    except Exception as e:
        print("comparing g1 with non graph type should not raise exception")

    #__ne__ test
    print_if_error("g1 != g1 should be False", (g1 != g1), False)
    print_if_error("g1 != g2 should be True", (g1 != g2), True)
    print_if_error("g1 != g3 should be True", (g1 != g3), True)
    
def test_add_sub()->None:
    g1 = create_example_graph()
    g3 = Graph(list(range(1, 15)), [(1, 3), (2, 3), (3, 4), (3, 5), #g3 has an additional vertex
                            (6, 7), (6, 8), (7, 8),
                            (9, 10), (10, 11), (11, 12), (12, 13)]) 

    #__add__ test
    g_plus = g1 + 14
    print_if_error("operator add should not modify original graph", g1, create_example_graph())
    print_if_error("operator add should not modify original graph", len(g1), len(create_example_graph()))

    print_if_error("new graph should have an additional vertex", len(g_plus), 14)
    print_if_error("new graph should match graph g3", (g_plus == g3), True)
    
    g_id_test = g1 + 140

    print_if_error("new graph should have an additional vertex", len(g_id_test), 14)
    print_if_error("new graph should not match graph g3", (g_id_test != g3), True)
    
    g_right = 14 + g1

    print_if_error("right addition does not match left addition", (g_plus == g_right), True)
    

    #__sub__ test
    g1 = create_example_graph()
    g4 = Graph([1,2] + list(range(4,14)), [#g4 has vertex 3 removed from the graph 
                            (6, 7), (6, 8), (7, 8),
                            (9, 10), (10, 11), (11, 12), (12, 13)]) 

    g_minus = g1 - 3
    print_if_error("operator subtract should not modify original graph", g1, create_example_graph())
    print_if_error("operator subtract should not modify original graph", len(g1), len(create_example_graph()))

    print_if_error("subtracting vertex 3 should reduce vertex size by 1", len(g_minus), 12)
    print_if_error("subtracting vertex 3 does not create node induced subgraph", (g_minus == g4), True)

    try:
        g_invalid = g1 - 100
    except KeyError as e:
        pass
    else:
        print("subtracting vertex (id=100) not in Graph should raise a KeyError")
    
    #Note: g = 3 - g1 is invalid because subtraction does not commute like addition

    #extra for experts: NOT graded
    #if you attempt this, make sure it doesn't break subtracting an individual vertex
    #g_minus_component = g1 - {1, 2, 3, 4, 5}

def test_setitem_getitem()->None:
    g1 = create_example_graph()
    g2 = Graph(vertices, [(1, 3), (2, 3), (3, 4), (3, 5), 
                            (6, 7), (6, 8), #g2 is missing (7, 8) from g1
                            (9, 10), (10, 11), (11, 12), (12, 13)])
    g1[7] = [(6, 7)]
    print_if_error("setitem should modify original graph", (g1 == create_example_graph()), False)
    print_if_error("vertex 7 of g1 should only have edge (6, 7)", (g1 == g2), True)

    try:
        g1[100] = []
    except KeyError as e:
        pass
    else:
        print("setitem on vertex (id=100) not in Graph should raise a KeyError")

    g1 = create_example_graph()
    print_if_error("getitem for vertex 3 incorrect", g1[3], [(3, 1), (3, 2), (3, 4), (3, 5)])

    try:
        g1[100]
    except KeyError as e:
        pass
    else:
        print("getitem on vertex id=100 not in Graph should raise a KeyError")

if __name__ == "__main__":
    print("example graph test")
    g1 = create_example_graph()
    verify_example_graph(g1)
    test_equality()
    test_add_sub()
    test_setitem_getitem()
    #your tests here
    pass
