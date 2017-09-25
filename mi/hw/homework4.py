from vertex import Vertex


class Graph():
    ''' Undirected, colorable Graph '''
    
    def __init__(self, vertex_nums:[int], edges_to_add:[(int,int)] = []):
        self.vertices = dict()
        for item in vertex_nums:
            v = Vertex(item)
            self.vertices[item] = v
        
        # TODO:  modify this constructor so that edges_to_add
        #        are also included in the Graph
        for edges in edges_to_add:
            vertex1 = edges[0]
            vertex2 = edges[1]
            self.vertices[vertex1].add_edge(self.vertices[vertex2])
            self.vertices[vertex2].add_edge(self.vertices[vertex1])



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

    def __str__(self):
        '''
        __str__() returns a string representation of the graph as follows:
        "Graph(v1, v2, v3, . . . vn), components={n}"
        where v1, v2, v3, vn, etc. are the vertex ID numbers,
        and v1 through vn are sorted in ascending order,
        and n is the result of count_components
        '''
        vertex_nums = list(self.vertices.keys())
        vertex_nums.sort()
        vertex_nums = [str(num) for num in vertex_nums]
        n = self.count_components()
        return "Graph(%s), components=%s" % (", ".join(vertex_nums), n)
    
    def __repr__(self):
        '''
        __repr__() returns a string representation of the graph as follows:
        "Graph([v1, v2, v3, . . . vn], [(v1, v2), (v2, v3), (v3, vn)])"
        where v1, v2, v3, vn, etc. are the vertex ID numbers,
        where v1 through vn (in the list of vertex ID numbers) are sorted in ascending order,
        where (v1, v2), (v2, v3), etc. are the edges in the graph,
        where the edges tuples are sorted in ascending order by the first vertex ID number,
            # so (1, 2) comes before (3, 10) comes before (4, 6)
        and where the edges tuples are further sorted in ascending order by the second vertex ID number.
            # so (1, 2) comes before (1, 4) comes before (1, 10)
        '''
        #eval(repr(x)) == x
        vertex_nums = list(self.vertices.keys())
        vertex_nums.sort()
        vertex_nums = [str(num) for num in vertex_nums]
        edges = []
        for vertex_num, vertex in self.vertices.items():
            neighbors = vertex.get_neighbors()
            for neighbor in neighbors:
                edge = tuple(sorted([vertex_num, neighbor.get_num()]))
                if edge not in edges:
                    edges.append(edge)
        edges = sorted(edges)
        return "Graph([%s], %s)" % (", ".join(vertex_nums), str(edges))


    
    def __eq__(self, other:'Graph'):
        '''
        __eq__() returns true if this Graph instance
        is equal to the provided Graph instance,
        false otherwise.
        Equality is met if both graphs have
        the same vertices (as determined by vertex ID numbers)
        and the same edges connecting those vertices.
        color and visit values do not affect equality
        '''
        if not isinstance(other, Graph):
            return False
        return self.__repr__() == other.__repr__()
    
    def __ne__(self, other:'Graph'):
        '''
        __ne__() returns true if this Graph instance
        is not equal to the provided Graph instance,
        false otherwise.
        Equality is met if both graphs have
        the same vertices (as determined by vertex ID numbers)
        and the same edges connecting those vertices.
        color and visit values do not affect equality
        '''
        #Hint: Write this in one line
        return not self.__eq__(other)

    def __add__(self, vertex_id:int):
        '''
        __add__() creates a new vertex in the graph
        with the provided ID number
        and no edges connecting it to other vertices
        '''
        vertex_nums = list(self.vertices.keys())
        vertex_nums.sort()
        edges = []
        for vertex_num, vertex in self.vertices.items():
            neighbors = vertex.get_neighbors()
            for neighbor in neighbors:
                edge = tuple(sorted([vertex_num, neighbor.get_num()]))
                if edge not in edges:
                    edges.append(edge)
        edges = sorted(edges)
        vertex_nums.append(vertex_id)
        return Graph(vertex_nums, edges)


    def __radd__(self, vertex_id:int):
        return self.__add__(vertex_id)

    
    def __sub__(self, vertex_id:int):
        '''
        __sub__() removes the vertex identified by
        the provided ID number from the graph,
        as well as all edges connecting it
        '''
        vertex_nums = list(self.vertices.keys())
        vertex_nums.sort()
        edges = []
        for vertex_num, vertex in self.vertices.items():
            neighbors = vertex.get_neighbors()
            for neighbor in neighbors:
                edge = tuple(sorted([vertex_num, neighbor.get_num()]))
                if edge not in edges:
                    edges.append(edge)
        edges = sorted(edges)
        if vertex_id in vertex_nums:
            vertex_nums.remove(vertex_id)
            temp = []
            for edge in edges:
                if vertex_id not in edge:
                    temp.append(edge)
            edges = temp
            return Graph(vertex_nums, edges)
        else:
            raise KeyError("vertex %s not in Graph" % vertex_id)

    def __iter__(self):
        '''
        __iter__() returns an iterable object
        that implements the __next__() function
        and initializes any necessary data structures 
        for the __next__() function.
        Mutating the graph should have no effect on 
        an iterator created prior to the change. 
        '''
        return self
    
    def __next__(self):
        '''
        __next__() should return each vertex of the graph
        in descending order of vertex id.
        raise StopIteration after all vertices have been returned
        '''
        vertex_nums = self.vertices.keys()
        vertex_nums.sort()
        for vertex_id in vertex_nums:
            yield self.vertices[vertex_id]
        

    def __setitem__(self, key, value:[(int,int)]):
        '''
        __setitem__() replaces the edges of the vertex given by key
        with the list of edge tuples given by value
        If any part of the arguments is valid
        (key not in graph, edges between vertices not in the graph)
        then this function should raise KeyError with an appropriate message
        '''
        if key not in self.vertices:
            raise KeyError("Key %s not in the Graph" % key)
        neighbors = self.vertices[key].get_neighbors()
        for edge in value:
            for point in edge:
                if point not in self.vertices:
                    raise KeyError("Vertex %s not in the Graph" % point)
        # remove old edges
        for neighbor in neighbors:
            self.vertices[key].remove_edge(neighbor)
            self.vertices[neighbor.get_num()].remove_edge(self.vertices[key])
        # add new edges
        for edge in value:
            self.vertices[edge[0]].add_edge(self.vertices[edge[1]])
            self.vertices[edge[1]].add_edge(self.vertices[edge[0]])


    def __getitem__(self, key):
        '''
        __getitem__() returns the list of edges incident to the vertex given by key.
        If the key does not refer to a valid vertex in the graph,
        then this function should raise KeyError with an appropriate message
        '''
        if key not in self.vertices:
            raise KeyError("Key %s is not in the Graph" % key)
        neighbors = self.vertices[key].get_neighbors()
        neighbors = [neighbor.get_num() for neighbor in neighbors]
        res = []
        for neighbor in neighbors:
            res.append((key, neighbor))
        return sorted(res)


    #Do NOT submit these functions unless you have written them correctly
    #submitting incorrect functions here will cause all tests to fail
    ##def __setattr__(self, name, value):
        ##pass

    ##def __getattr__(self, name):
        ##pass

