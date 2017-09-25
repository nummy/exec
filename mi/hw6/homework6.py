from vertex import Vertex
from _collections_abc import Iterable

def fibonacci()->int:
    '''
    fibonacci() is a generator that outputs the next fibonacci number
    on each call of next()
    fib(1) = 1, fib(2) = 1
    for i > 2, fib(i) = fib(i-1) + fib(i-2)
    example:fib(3) = fib(2) + fib(1) = 1 + 1 = 2
    fib(4) = fib(3) + fib(2) = 2 + 1 = 3
    '''
    a = 1
    b = 1
    yield 1
    while True:
        a, b = b, a+b
        yield a


class Graph():
    ''' Undirected, colorable Graph '''
    def __init__(self, vertex_nums:[int], edges_to_add:[(int,int)] = []):
        self.vertices = dict()
        for item in vertex_nums:
            v = Vertex(item)
            self.vertices[item] = v
        
        # TODO:  modify this constructor so that edges_to_add
        #        are also included in the Graph
        for edge in edges_to_add:
            self.add_edge(edge[0], edge[1])

    def add_edge(self, source: int, dest: int)->None:
        ''' 
        add_edge() connects the source and the destination vertices 
        '''
        self.vertices[source].add_edge(self.vertices[dest])
        self.vertices[dest].add_edge(self.vertices[source])

    def degree(self, vertex_id:int)->int:
        '''
        degree() returns the number of neighbors
        of the vertex with the given id
        '''
        return len(self.vertices[vertex_id].get_neighbors())

    def _breadth_first_search(self, vertex_id:int)->int:
        '''
        _breadth_first_search() returns the number of vertices 
        in the connected component of the given vertex,
        including the starting vertex
        NOTE:  does not reset the "visited" counter on the vertex objects
        '''
        vertices_to_examine = [self.vertices[vertex_id]] # the list of vertices that still need to be examined
        component_size = 0 # running counter of component size
        
        # walk the component until no more unvisited vertices to inspect
        while len(vertices_to_examine) > 0:
            current_vertex = vertices_to_examine.pop(0) # remove the first vertex from the list
            current_vertex.visit()
            component_size += 1
            
            # for each neighbor, add to the to-inspect list if not already visited
            for item in current_vertex.get_neighbors():
                if not item.is_visited() and not item in vertices_to_examine:
                    vertices_to_examine.append(item)        
        return component_size
    
    def _reset_vertices(self):
        '''
        _reset_vertices() resets the "visited" counter 
        on all vertex objects in the graph
        '''
        for key, item in self.vertices.items():
            item.reset()

    def component_size(self, vertex_id:int)->int:
        '''
        component_size() returns the number of vertices 
        in the connected component of the given vertex,
        including the starting vertex
        '''
        self._reset_vertices()
        return self._breadth_first_search(vertex_id)

    def count_components(self)->int:
        '''
        count_components() returns the number of connected components
        in the graph
        '''
        self._reset_vertices()

        component_count = 0        
        for key, item in self.vertices.items():  
            if not item.is_visited():  # if this vertex is not in a previously visited component
                self._breadth_first_search(key)  # then search this vertex's component, thereby marking all members as visited
                component_count += 1            
        
        return component_count
    
    def __len__(self)->int:
        '''
        __len__() returns the number of vertices in the graph
        '''
        return len(self.vertices)

    def __iter__(self):
        '''
        __iter__() returns an iterable object
        that implements the __next__() function
        and initializes any necessary data structures 
        for the __next__() function.
        Mutating the graph should have no effect on 
        an iterator created prior to the change. 
        '''
        self.vertex_nums = sorted(self.vertices.keys(), reverse=True)
        self.index = 1
        return self
    
    def __next__(self):
        '''
        __next__() should return each vertex of the graph
        in descending order of vertex id.
        raise StopIteration after all vertices have been returned
        '''
        if self.index > len(self.vertex_nums):
            raise StopIteration()
        vertex = self.vertices[self.vertex_nums[self.index-1]]
        self.index += 1
        return vertex.get_num()

        

class ConnectedVertices:
    '''
    decorator for iterable that iterates only over vertices
    of a graph that are connected to at least one other vertex
    '''

    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        '''
        an iterator over vertices with at least one edge
        '''
        lst = []
        for vertex in self.iterable:
            if len(self.iterable.vertices[vertex].get_neighbors()) != 0:
                lst.append(vertex)
        return iter(lst)


class Components:
    '''
    decorator for iterable that iterates over a single vertex
    of each component in the graph
    '''
    
    def __init__(self, iterable):
        self.iterable = iterable
        
    def __iter__(self):
        '''
        an iterator over a single vertex of each component
        '''
        self.iterable._reset_vertices()
        lst = []
        vertices = list(self.iterable)
        vertices.reverse()
        for vertex in vertices:
            if not self.iterable.vertices[vertex].is_visited():
                lst.append(vertex)
                self.iterable._breadth_first_search(vertex)
        lst.reverse()
        return iter(lst)

def get_first_n_digit_prime(n:int):
    '''
    get_first_n_digit_prime() is a generator that outputs
    the first n prime numbers with a unique number of digits.
    Specifically, each next() call to the generator should
    yield the next largest prime number with a new number of
    digits.  The generator should yield these prime numbers
    up to a maximum number of digits defined by the input parameter.
    For example, with the input parameter of 5,
    next(theGenerator) should yield 2 (the smallest 1-digit prime).
    Then next(theGenerator) should yield 11 (the smallest 2-digit prime).
    Then next(theGenerator) should yield 101 (the smallest 3-digit prime).
    Then next(theGenerator) should yield 1009 (the smallest 4-digit prime).
    Then next(theGenerator) should yield 10007 (the smallest 5-digit prime).
    Then next(theGenerator) should raise a StopIteration exception.
    '''
    num_of_digits = 1
    while True:
        if num_of_digits == 1:
            num_of_digits += 1
            yield 2
        if num_of_digits > n:
            raise StopIteration()
        num = pow(10, num_of_digits-1)
        prime = 2
        while num < pow(10, num_of_digits):
            flag = True
            for i in range(2, num):
                if num%i == 0:
                    flag = False
                    break
            num += 1
            if flag:
                prime = num - 1
                break
        num_of_digits += 1
        yield prime

if __name__ == "__main__":
    vertices = list(range(1,9))
    g1 = Graph(vertices, [(1,3), (3,5), (3,4), (7,8)])
    g2 = ConnectedVertices(g1)
    for vertex in g2:
        print(vertex)
    g3 = Components(g1)
    for vertex in g3:
        print(vertex)
    primes = get_first_n_digit_prime(5)
    print(next(primes))
    print(next(primes))
    print(next(primes))
    print(next(primes))
    print(next(primes))
    print(next(primes))