from vertex import Vertex
from homework5 import *

def print_if_error(description:str, result, expected)->None:
    if not (expected == result):
        print(description)
        print("Expected:   ", expected)
        print("Result:     ", result)        

def verify_elementwise(result: tuple, expected: tuple)->bool:
    return len(result) == len(expected) and \
        result[0] == expected[0] and \
        all([(x == a) and (y == b) for (x, y), (a, b) in zip(result[0], expected[1])])

def example_undirected()->UndirectedGraph:
    vertices = list(range(1,14))
    g1 = UndirectedGraph(vertices, [(1, 3), (2, 3), (3, 4), (3, 5), 
                            (6, 7), (6, 8), (7, 8)])
    g1.add_edge(9, 10)
    g1.add_edge(10, 11)
    g1.add_edge(11, 12)
    g1.add_edge(12, 13)
    #see picture of given test graph
    return g1

def test_undirected(g1:UndirectedGraph)->None:
    print_if_error("path from 1 to 2 not found", 
        g1.calculate_fewest_edges_path(1, 2), (2, [(1, 3), (3, 2)]))
    print_if_error("path from 1 to 3 not found", 
        g1.calculate_fewest_edges_path(1, 3), (1, [(1, 3)]))
    print_if_error("path from 1 to 4 not found", 
        g1.calculate_fewest_edges_path(1, 4), (2, [(1, 3), (3, 4)]))
    print_if_error("path from 1 to 5 not found", 
        g1.calculate_fewest_edges_path(1, 5), (2, [(1, 3), (3, 5)]))

    print_if_error("no path should exist from 1 to 6", 
        g1.calculate_fewest_edges_path(1, 6), (-1, []))
    print_if_error("no path should exist from 6 to 13", 
        g1.calculate_fewest_edges_path(6, 13), (-1, []))
    print_if_error("no path should exist from 9 to 3", 
        g1.calculate_fewest_edges_path(9, 3), (-1, []))
    
    print_if_error("path from 13 to 9 not found", 
        g1.calculate_fewest_edges_path(13, 9), (4, [(13, 12), (12, 11), (11, 10), (10, 9)]))


def example_undirected_weighted()->WeightedUndirectedGraph:
    vertices = list(range(1,14))
    g1 = WeightedUndirectedGraph(vertices, [(1, 3, 2), (2, 3, 1), (3, 4, -1), (3, 5, -2), 
                            (6, 7, -1), (6, 8, -2), (7, 8, 1)])
    g1.add_edge(9, 10, 1)
    g1.add_edge(10, 11, 1)
    g1.add_edge(11, 12, 1)
    g1.add_edge(12, 13, 1) 

    return g1

def test_undirected_weighted(g1:WeightedUndirectedGraph)->None:
    print_if_error("path from 1 to 2 incorrect", 
        g1.calculate_fewest_edges_path(1, 2), (3, [(1, 3), (3, 2)]))
    print_if_error("path from 1 to 3 incorrect", 
        g1.calculate_fewest_edges_path(1, 3), (2, [(1, 3)]))
    print_if_error("path from 1 to 4 incorrect", 
        g1.calculate_fewest_edges_path(1, 4), (1, [(1, 3), (3, 4)]))
    print_if_error("path from 1 to 5 incorrect", 
        g1.calculate_fewest_edges_path(1, 5), (0, [(1, 3), (3, 5)]))


    print_if_error("no path should exist from 1 to 6", 
        g1.calculate_fewest_edges_path(1, 6), (-1, []))
    print_if_error("no path should exist from 6 to 13", 
        g1.calculate_fewest_edges_path(6, 13), (-1, []))
    print_if_error("no path should exist from 9 to 3", 
        g1.calculate_fewest_edges_path(9, 3), (-1, []))
    
    print_if_error("path from 13 to 9 incorrect", 
        g1.calculate_fewest_edges_path(13, 9), (4, [(13, 12), (12, 11), (11, 10), (10, 9)]))

def acyclic_directed()->DirectedGraph:
    g1 = DirectedGraph([31, 32, 33, 45, 46, 161, 51, 53, 6, 7, 139], 
        [(31, 32), (32, 33), (33, 45), (45, 46), (46, 161)])

    g1.add_edge(31, 51)
    g1.add_edge(51, 53)
    g1.add_edge(6, 51)
    g1.add_edge(6, 7)
    g1.add_edge(6, 161)
    g1.add_edge(7, 161)

    return g1

def test_acyclic(g1:DirectedGraph):
    print_if_error("prerequisite of 31 for 32", 
        g1.calculate_fewest_edges_path(31, 32), (1,[(31, 32)]))
    print_if_error("prerequisite of 31 for 33", 
        g1.calculate_fewest_edges_path(31, 33), (2,[(31, 32), (32, 33)]))
    print_if_error("prerequisite of 31 for 161", 
        g1.calculate_fewest_edges_path(31, 161), 
            (5,[(31, 32), (32, 33), (33, 45), (45, 46), (46, 161)]))
    print_if_error("prerequisite of 31 for 53", 
        g1.calculate_fewest_edges_path(31, 53), 
            (2,[(31, 51), (51, 53)]))

    print_if_error("prerequisite of 51 for 53", 
        g1.calculate_fewest_edges_path(51, 53), (1,[(51, 53)]))
    print_if_error("prerequisite of 6 for 7", 
        g1.calculate_fewest_edges_path(6, 7), (1,[(6, 7)]))
    print_if_error("prerequisite of 6 for 53", 
        g1.calculate_fewest_edges_path(6, 53), (2,[(6, 51), (51, 53)]))
    print_if_error("prerequisite of 6 for 161", 
        g1.calculate_fewest_edges_path(6, 161), (1,[(6, 161)]))

    print_if_error("31 not required for 6", 
        g1.calculate_fewest_edges_path(31, 6), (-1, []))
    print_if_error("6 not required for 31", 
        g1.calculate_fewest_edges_path(6, 31), (-1, []))
    print_if_error("51 not required for 32", 
        g1.calculate_fewest_edges_path(51, 32), (-1, []))
    print_if_error("45 not required for 7", 
        g1.calculate_fewest_edges_path(45, 7), (-1, []))
    print_if_error("7 not required for 45", 
        g1.calculate_fewest_edges_path(7, 45), (-1, []))
    print_if_error("53 not required for 139", 
        g1.calculate_fewest_edges_path(53, 139), (-1, []))

    print_if_error("relationship should be directional 32, 31", 
        g1.calculate_fewest_edges_path(32, 31), (-1, []))
    print_if_error("relationship should be directional 46, 31", 
        g1.calculate_fewest_edges_path(46, 31), (-1, []))
    print_if_error("relationship should be directional 46, 45", 
        g1.calculate_fewest_edges_path(46, 45), (-1, []))
    print_if_error("relationship should be directional 161, 6", 
        g1.calculate_fewest_edges_path(161, 6), (-1, []))
    print_if_error("relationship should be directional 161, 7", 
        g1.calculate_fewest_edges_path(161, 7), (-1, []))
    print_if_error("relationship should be directional 7, 6", 
        g1.calculate_fewest_edges_path(7, 6), (-1, []))

    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 6), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 7), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 31), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 32), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 33), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 45), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 46), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 161), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 51), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 53), (-1, []))


def acyclic_directed_weighted()->WeightedDirectedGraph:
    g1 = WeightedDirectedGraph([31, 32, 33, 45, 46, 161, 51, 53, 6, 7, 139], 
        [(31, 32, 2), (32, 33, 2), (33, 45, 2), (45, 46, 2), (46, 161, 2)])

    g1.add_edge(31, 51, 1)
    g1.add_edge(51, 53, 1)
    g1.add_edge(6, 51, 1)
    g1.add_edge(6, 7, 1)
    g1.add_edge(6, 161, 1)
    g1.add_edge(7, 161, 1)

    return g1

def test_acyclic_weighted(g1:WeightedDirectedGraph):
    print_if_error("prerequisite of 31 for 32", 
        g1.calculate_fewest_edges_path(31, 32), (2,[(31, 32)]))
    print_if_error("prerequisite of 31 for 33", 
        g1.calculate_fewest_edges_path(31, 33), (4,[(31, 32), (32, 33)]))
    print_if_error("prerequisite of 31 for 161", 
        g1.calculate_fewest_edges_path(31, 161), 
            (10,[(31, 32), (32, 33), (33, 45), (45, 46), (46, 161)]))
    print_if_error("prerequisite of 31 for 53", 
        g1.calculate_fewest_edges_path(31, 53), 
            (2,[(31, 51), (51, 53)]))

    print_if_error("prerequisite of 51 for 53", 
        g1.calculate_fewest_edges_path(51, 53), (1,[(51, 53)]))
    print_if_error("prerequisite of 6 for 7", 
        g1.calculate_fewest_edges_path(6, 7), (1,[(6, 7)]))
    print_if_error("prerequisite of 6 for 53", 
        g1.calculate_fewest_edges_path(6, 53), (2,[(6, 51), (51, 53)]))
    print_if_error("prerequisite of 6 for 161", 
        g1.calculate_fewest_edges_path(6, 161), (1,[(6, 161)]))

    print_if_error("31 not required for 6", 
        g1.calculate_fewest_edges_path(31, 6), (-1, []))
    print_if_error("6 not required for 31", 
        g1.calculate_fewest_edges_path(6, 31), (-1, []))
    print_if_error("51 not required for 32", 
        g1.calculate_fewest_edges_path(51, 32), (-1, []))
    print_if_error("45 not required for 7", 
        g1.calculate_fewest_edges_path(45, 7), (-1, []))
    print_if_error("7 not required for 45", 
        g1.calculate_fewest_edges_path(7, 45), (-1, []))
    print_if_error("53 not required for 139", 
        g1.calculate_fewest_edges_path(53, 139), (-1, []))

    print_if_error("relationship should be directional 32, 31", 
        g1.calculate_fewest_edges_path(32, 31), (-1, []))
    print_if_error("relationship should be directional 46, 31", 
        g1.calculate_fewest_edges_path(46, 31), (-1, []))
    print_if_error("relationship should be directional 46, 45", 
        g1.calculate_fewest_edges_path(46, 45), (-1, []))
    print_if_error("relationship should be directional 161, 6", 
        g1.calculate_fewest_edges_path(161, 6), (-1, []))
    print_if_error("relationship should be directional 161, 7", 
        g1.calculate_fewest_edges_path(161, 7), (-1, []))
    print_if_error("relationship should be directional 7, 6", 
        g1.calculate_fewest_edges_path(7, 6), (-1, []))

    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 6), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 7), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 31), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 32), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 33), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 45), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 46), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 161), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 51), (-1, []))
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 53), (-1, []))

def cyclic_directed()->DirectedGraph:
    vertices = list(range(1,17))
    g1 = DirectedGraph(vertices, [(9, 10), (10, 9), (9, 11), (11, 9),
        (9, 6), (6, 3), (3, 2), (2, 1), 
        (1, 5), (5, 15), (15, 16), (16, 1)])
    g1.add_edge(11, 12)
    g1.add_edge(12, 11)
    g1.add_edge(10, 12)
    g1.add_edge(12, 10)
    g1.add_edge(1, 4)
    g1.add_edge(4, 7)
    g1.add_edge(7, 8)
    g1.add_edge(8, 9)
    return g1

def test_cyclic(g1:DirectedGraph):
    print_if_error("path from 7 to 8 incorrect", 
        g1.calculate_fewest_edges_path(7, 8), (1, [(7, 8)]))
    print_if_error("path from 16 to 1 incorrect", 
        g1.calculate_fewest_edges_path(16, 1), (1, [(16, 1)]))

    print_if_error("path from 11 to 4 incorrect", 
        g1.calculate_fewest_edges_path(11, 4), 
        (6, [(11, 9), (9, 6), (6, 3), (3, 2), (2, 1), (1, 4)]))
    print_if_error("path from 5 to 11 incorrect", 
        g1.calculate_fewest_edges_path(5, 11), 
        (8, [(5, 15), (15, 16), (16, 1), (1, 4), (4, 7), (7, 8), (8, 9), (9, 11)]))

    print_if_error("path should be unidirectional (9, 6)", 
        g1.calculate_fewest_edges_path(9, 6), 
        (1, [(9, 6)]))
    print_if_error("path should be unidirectional (6, 9)", 
        g1.calculate_fewest_edges_path(6, 9), 
        (7, [(6, 3), (3, 2), (2, 1), (1, 4), (4, 7), (7, 8), (8, 9)]))

    print_if_error("path should be bidirectional (11, 12)", 
        g1.calculate_fewest_edges_path(11, 12), 
        (1, [(11, 12)]))
    print_if_error("path should be bidirectional (12, 11)", 
        g1.calculate_fewest_edges_path(12, 11), 
        (1, [(12, 11)]))
    
def cyclic_directed_weighted()->WeightedDirectedGraph:
    vertices = list(range(1,17))
    g1 = WeightedDirectedGraph(vertices, 
        [(9, 10, 1), (10, 9, -1), (9, 11, 2), (11, 9, -2), 
        (9, 6, -3), (6, 3, -3), (3, 2, -1), (2, 1, -1), 
        (1, 5, 4), (5, 15, 10), (15, 16, 1), (16, 1, -15)])
    g1.add_edge(11, 12, 1)
    g1.add_edge(12, 11, -1)
    g1.add_edge(10, 12, 2)
    g1.add_edge(12, 10, -2)
    g1.add_edge(1, 4, 3)
    g1.add_edge(4, 7, 3)
    g1.add_edge(7, 8, 1)
    g1.add_edge(8, 9, 1)
    return g1

def test_cyclic_weighted(g1:WeightedDirectedGraph):
    print_if_error("path from 7 to 8 incorrect", 
        g1.calculate_fewest_edges_path(7, 8), (1, [(7, 8)]))
    print_if_error("path from 16 to 1 incorrect", 
        g1.calculate_fewest_edges_path(16, 1), (-15, [(16, 1)]))

    print_if_error("path from 11 to 4 incorrect", 
        g1.calculate_fewest_edges_path(11, 4), 
        (-7, [(11, 9), (9, 6), (6, 3), (3, 2), (2, 1), (1, 4)]))
    print_if_error("path from 5 to 11 incorrect", 
        g1.calculate_fewest_edges_path(5, 11), 
        (6, [(5, 15), (15, 16), (16, 1), (1, 4), (4, 7), (7, 8), (8, 9), (9, 11)]))

    print_if_error("path should be unidirectional (9, 6)", 
        g1.calculate_fewest_edges_path(9, 6), 
        (-3, [(9, 6)]))
    print_if_error("path should be unidirectional (6, 9)", 
        g1.calculate_fewest_edges_path(6, 9), 
        (3, [(6, 3), (3, 2), (2, 1), (1, 4), (4, 7), (7, 8), (8, 9)]))

    print_if_error("path should be bidirectional (11, 12)", 
        g1.calculate_fewest_edges_path(11, 12), 
        (1, [(11, 12)]))
    print_if_error("path should be bidirectional (12, 11)", 
        g1.calculate_fewest_edges_path(12, 11), 
        (-1, [(12, 11)]))
    
def example_undirected_weighted_costed()->WeightedCostedUndirectedGraph:
    vertices = list(range(1,14))
    g1 = WeightedCostedUndirectedGraph(vertices, 
        [(1, 3, 2, 4), (2, 3, 1, 5), (3, 4, -1, 7), (3, 5, -2, 8), 
        (6, 7, -1, 13), (6, 8, -2, 14), (7, 8, 1, 15)])

    g1.add_edge(9, 10, 1, 19)
    g1.add_edge(10, 11, 1, 20)
    g1.add_edge(11, 12, 1, 21)
    g1.add_edge(12, 13, 1, 22) 

    return g1

def acyclic_directed_weighted_costed()->WeightedCostedDirectedGraph:
    g1 = WeightedCostedDirectedGraph([31, 32, 33, 45, 46, 161, 51, 53, 6, 7, 139], 
        [(31, 32, 2, 4), (32, 33, 2, 4), (33, 45, 2, 4), (45, 46, 2, 4), (46, 161, 2, 4)])

    g1.add_edge(31, 51, 1, 4)
    g1.add_edge(51, 53, 1, 4)
    g1.add_edge(6, 51, 1, 4)
    g1.add_edge(6, 7, 1, 4)
    g1.add_edge(6, 161, 1, 4)
    g1.add_edge(7, 161, 1, 4)

    return g1

def cyclic_directed_weighted_costed()->WeightedCostedDirectedGraph:
    vertices = list(range(1,17))
    g1 = WeightedCostedDirectedGraph(vertices, 
        [(9, 10, 1, 19), (10, 9, -1, 1), (9, 11, 2, 20), (11, 9, -2, 2), 
        (9, 6, -3, 15), (6, 3, -3, 9), (3, 2, -1, 5), (2, 1, -1, 3), 
        (1, 5, 4, 6), (5, 15, 10, 20), (15, 16, 1, 31), (16, 1, -15, 17)])
    g1.add_edge(11, 12, 1, 1)
    g1.add_edge(12, 11, -1, 23)
    g1.add_edge(10, 12, 2, 22)
    g1.add_edge(12, 10, -2, 2)
    g1.add_edge(1, 4, 3, 5)
    g1.add_edge(4, 7, 3, 11)
    g1.add_edge(7, 8, 1, 15)
    g1.add_edge(8, 9, 1, 17)
    return g1

def test_undirected_weighted_costed(g1:WeightedCostedUndirectedGraph):
    print_if_error("path from 13 to 9 incorrect", 
        g1.calculate_fewest_edges_path(13, 9), ((4/82), [(13, 12), (12, 11), (11, 10), (10, 9)]))

def test_acyclic_weighted_costed(g1:WeightedCostedDirectedGraph):
    print_if_error("139 has no relationship to any other vertex", 
        g1.calculate_fewest_edges_path(139, 6), (-1, []))

def test_cyclic_weighted_costed(g1:WeightedCostedDirectedGraph):
    print_if_error("path from 7 to 8 incorrect", 
        g1.calculate_fewest_edges_path(7, 8), ((1/15), [(7, 8)]))

if __name__ == "__main__":
    test_undirected(example_undirected())
    test_acyclic(acyclic_directed())
    test_cyclic(cyclic_directed())

    test_undirected_weighted(example_undirected_weighted())
    test_acyclic_weighted(acyclic_directed_weighted())
    test_cyclic_weighted(cyclic_directed_weighted())

    test_undirected_weighted_costed(example_undirected_weighted_costed())
    test_acyclic_weighted_costed(acyclic_directed_weighted_costed())
    test_cyclic_weighted_costed(cyclic_directed_weighted_costed())
