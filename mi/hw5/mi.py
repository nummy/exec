from vertex import Vertex


class UndirectedGraph():
    ''' an undirected graph '''

    def __init__(self, vertex_nums:[int], edges_to_add:[(int,int)] = []):
        self.vertices = dict()
        for item in vertex_nums:
            v = Vertex(item)
            self.vertices[item] = v

        for item in edges_to_add:
            self.vertices[item[0]].add_edge(self.vertices[item[1]], 1)
            self.vertices[item[1]].add_edge(self.vertices[item[0]], 1)

    def add_edge(self, source: int, dest: int)->None:
        '''
        add_edge() connects the source and the destination vertices
        '''
        self.vertices[source].add_edge(self.vertices[dest], 1)
        self.vertices[dest].add_edge(self.vertices[source], 1)

    def calculate_fewest_edges_path(self, source: int, dest: int)-> (float, [(int, int)]):
        '''
        + calculate_fewest_edges_path() calculates the shortest path
        between two vertices in the graph.
        + The shortest path is the path with the fewest number of edges
        traversed from the source to the destination.
        + If there are multiple such paths, any one can be returned.
        + The return value is a tuple of (# of edges, [list of edges]).
        + The # of edges is the number of edges traversed on the shortest path.
        + The list of edges is a list of tuples containing the vertex ids on the path
        from the source to the destination.  The list should be in the order that
        the edges are traversed along the path from the source to the destination.
        Each tuple should be ordered (source, dest) to show the direction of
        traversal.
        + If no path connects the source and destination, the function
        returns (-1, []).
        '''
        #TODO:  implement the calculate_fewest_edges_path() function.
        # use breadth first search algorithm here
        parent = {}   # use a dict to store predecessor of the vertex, ex v->w, parent[w]=v
        visited = [source] # visited vertex
        queue = [source]   # vertex to be visited
        while len(queue) > 0:
            # if all the vertex were visited, then jump out of the while loop
            vertex = queue[0]
            queue.remove(vertex)
            neighbors = self.vertices[vertex].get_neighbors()
            for neighbor in neighbors:
                neighbor_num = neighbor.get_num()
                if neighbor_num not in visited and neighbor_num not in queue:
                    parent[neighbor_num] = vertex
                    visited.append(neighbor_num)
                    queue.append(neighbor_num)
        if dest not in parent:
            # if no path connects the source and destination
            return -1, []
        edges = []  # store path
        while dest:
            predecessor = parent.get(dest, None)
            if predecessor == None:
                break
            edges.append((predecessor, dest))
            dest = predecessor
        edges.reverse()
        return len(edges), edges



class DirectedGraph():
    ''' a directed graph '''

    def __init__(self, vertex_nums:[int], edges_to_add:[(int,int)] = []):

        #TODO:  implement the constructor, taking a list of vertex id numbers
        #       and an optional list of edges.  An edge starts at the vertex
        #       identified by tuple[0] and ends at the vertex identified by tuple[1]
        self.vertices = dict()
        for item in vertex_nums:
            v = Vertex(item)
            self.vertices[item] = v

        for item in edges_to_add:
            self.vertices[item[0]].add_edge(self.vertices[item[1]], 1)

    def add_edge(self, source: int, dest: int)->None:
        '''
        add_edge() connects the source and the destination vertices
        '''
        #TODO:  implement the add_edge() function, adding a directed edge
        #       from the source vertex to the destination vertex
        self.vertices[source].add_edge(self.vertices[dest], 1)

    def calculate_fewest_edges_path(self, source: int, dest: int)-> (float, [(int, int)]):
        '''
        + calculate_fewest_edges_path() calculates the shortest path
        between two vertices in the graph.
        + The shortest path is the path with the fewest number of edges
        traversed from the source to the destination.
        + If there are multiple such paths, any one can be returned.
        + The return value is a tuple of (# of edges, [list of edges]).
        + The # of edges is the number of edges traversed on the shortest path.
        + The list of edges is a list of tuples containing the vertex ids on the path
        from the source to the destination.  The list should be in the order that
        the edges are traversed along the path from the source to the destination.
        Each tuple should be ordered (source, dest) to show the direction of
        traversal.
        + If no path connects the source and destination, the function
        returns (-1, []).
        + NOTE:  an edge can only be traversed in one direction, because this is a directed graph.
        '''
        parent = {}   # use a dict to store predecessor of the vertex, ex v->w, parent[w]=v
        visited = [source] # visited vertex
        queue = [source]   # vertex to be visited
        while len(queue) > 0:
            # if all the vertex were visited, then jump out of the while loop
            vertex = queue[0]
            queue.remove(vertex)
            neighbors = self.vertices[vertex].get_neighbors()
            for neighbor in neighbors:
                neighbor_num = neighbor.get_num()
                if neighbor_num not in visited and neighbor_num not in queue:
                    parent[neighbor_num] = vertex
                    visited.append(neighbor_num)
                    queue.append(neighbor_num)
        if dest not in parent:
            return -1, []
        edges = [] # store path
        while dest:
            predecessor = parent.get(dest, None)
            if predecessor == None:
                break
            edges.append((predecessor, dest))
            dest = predecessor
        edges.reverse()
        return len(edges), edges


class WeightedUndirectedGraph(UndirectedGraph):
    ''' a weighted, undirected graph 
    + Implement this class using inheritance.
    '''

    def __init__(self, vertex_nums:[int], edges_to_add:[(int,int, int)] = []):
        #TODO:  implement the constructor, taking a list of vertex id numbers
        #       and an optional list of edges.  An edge connects the vertex
        #       identified by tuple[0] with the vertex identified by tuple[1],
        #       and has  weight identified by tuple[2]
        self.vertices = dict()
        for item in vertex_nums:
            v = Vertex(item)
            self.vertices[item] = v

        for item in edges_to_add:
            self.vertices[item[0]].add_edge(self.vertices[item[1]], item[2])
            self.vertices[item[1]].add_edge(self.vertices[item[0]], item[2])


    def add_edge(self, source: int, dest: int, weight: int)->None:
        '''
        add_edge() connects the source and the destination vertices
        '''
        #TODO:  implement the add_edge() function, adding an undirected edge
        #       between the source vertex and the destination vertex with
        #       the specified weight
        self.vertices[source].add_edge(self.vertices[dest], weight)
        self.vertices[dest].add_edge(self.vertices[source], weight)

    def calculate_fewest_edges_path(self, source: int, dest: int)-> (float, [(int, int)]):
        '''
        + calculate_fewest_edges_path() calculates the shortest path between two
        vertices in the graph.
        + The shortest path is the path with the fewest number of edges
        traversed from the source to the destination.
        + If there are multiple such paths, any one can be returned.
        + The return values are (cummulative weight, [list of edges]).
        + The cummulative weight is the total weight accumulated when
        traversing the identified path.
        + The list of edges is a list of tuples containing the vertex ids on the path
        from the source to the destination.  The list should be in the order that
        the edges are traversed along the path from the source to the destination.
        Each tuple should be ordered (source, dest) to show the direction of
        traversal.
        + If no path connects the source and destination, the function
        returns (-1, []).
        '''
        #TODO:  implement the calculate_fewest_edges_path() function.
        num, edges = UndirectedGraph.calculate_fewest_edges_path(self, source, dest)
        if num == -1:
            # no path exist
            return -1, []
        sum_weight = 0 # cummulative weight
        for edge in edges:
            sum_weight += self.vertices[edge[0]].get_weight(self.vertices[edge[1]])
        return sum_weight, edges

class WeightedDirectedGraph(DirectedGraph):
    ''' an weighted, directed graph 
    + Implement this class using inheritance.
    '''

    def __init__(self, vertex_nums:[int], edges_to_add:[(int,int, int)] = []):
        #TODO:  implement the constructor, taking a list of vertex id numbers
        #       and an optional list of edges.  An edge starts at the vertex
        #       identified by tuple[0], ends at the vertex identified by tuple[1],
        #       and has  weight identified by tuple[2]
        self.vertices = dict()
        for item in vertex_nums:
            v = Vertex(item)
            self.vertices[item] = v

        for item in edges_to_add:
            self.vertices[item[0]].add_edge(self.vertices[item[1]], item[2])

    def add_edge(self, source: int, dest: int, weight: int)->None:
        '''
        add_edge() connects the source and the destination vertices
        '''
        #TODO:  implement the add_edge() function, adding a directed edge
        #       from the source vertex to the destination vertex with
        #       the specified weight
        self.vertices[source].add_edge(self.vertices[dest], weight)

    def calculate_fewest_edges_path(self, source: int, dest: int)-> (float, [(int, int)]):
        '''
        + calculate_fewest_edges_path() calculates the shortest path between two
        vertices in the graph.
        + The shortest path is the path with the fewest number of edges
        traversed from the source to the destination.
        + If there are multiple such paths, any one can be returned.
        + The return values are (cummulative weight, [list of edges]).
        + The cummulative weight is the total weight accumulated when
        traversing the identified path.
        + The list of edges is a list of tuples containing the vertex ids on the path
        from the source to the destination.  The list should be in the order that
        the edges are traversed along the path from the source to the destination.
        Each tuple should be ordered (source, dest) to show the direction of
        traversal.
        + If no path connects the source and destination, the function
        returns (-1, []).
        + NOTE:  an edge can only be traversed in one direction, because this is a directed graph.
        '''
        #TODO:  implement the calculate_fewest_edges_path() function.
        num, edges = DirectedGraph.calculate_fewest_edges_path(self, source, dest)
        if num == -1:
            # no path exist
            return -1, []
        sum_weight = 0 # cummulative weight
        for edge in edges:
            sum_weight += self.vertices[edge[0]].get_weight(self.vertices[edge[1]])
        return sum_weight, edges

class WeightedCostedUndirectedGraph(WeightedUndirectedGraph):
    ''' a weighted, costed, undirected graph 
    + Implement this class using inheritance.
    '''

    def __init__(self, vertex_nums:[int], edges_to_add:[(int,int, int, int)] = []):
        #TODO:  implement the constructor, taking a list of vertex id numbers
        #       and an optional list of edges.  An edge connects the vertex
        #       identified by tuple[0] with the vertex identified by tuple[1],
        #       and has  weight identified by tuple[2] and cost identified by tuple[3]
        WeightedUndirectedGraph.__init__(self, vertex_nums, edges_to_add)
        for item in edges_to_add:
            # init cost
            self.vertices[item[0]].set_cost(self.vertices[item[1]], item[3])
            self.vertices[item[1]].set_cost(self.vertices[item[0]], item[3])


    def add_edge(self, source: int, dest: int, weight: int, cost: int)->None:
        '''
        add_edge() connects the source and the destination vertices
        '''
        #TODO:  implement the add_edge() function, adding an undirected edge
        #       between the source vertex and the destination vertex with
        #       the specified weight and cost
        # add edge
        self.vertices[source].add_edge(self.vertices[dest], weight)
        self.vertices[dest].add_edge(self.vertices[source], weight)
        # set cost
        self.vertices[source].set_cost(self.vertices[dest], cost)
        self.vertices[dest].set_cost(self.vertices[source], cost)

    def calculate_fewest_edges_path(self, source: int, dest: int)-> (float, [(int, int)]):
        '''
        + calculate_fewest_edges_path() calculates the shortest path between two
        vertices in the graph.
        + The shortest path is the path with the fewest number of edges
        traversed from the source to the destination.
        + If there are multiple such paths, any one can be returned.
        + The return values are (cost ratio, [list of edges]).
        + The cost ratio is the total weight accumulated when
        traversing the identified path divided by the total cost accumulated when
        traversing the identified path:
        cost ratio = (cummulative weight) / (cummulative cost)
        + The list of edges is a list of tuples containing the vertex ids on the path
        from the source to the destination.  The list should be in the order that
        the edges are traversed along the path from the source to the destination.
        Each tuple should be ordered (source, dest) to show the direction of
        traversal.
        + If no path connects the source and destination, the function
        returns (-1, []).
        '''
        #TODO:  implement the calculate_fewest_edges_path() function.
        weight, edges = WeightedUndirectedGraph.calculate_fewest_edges_path(self, source, dest)
        if weight == -1:
            return -1, []
        sum_weight = 0 # cummulative weight
        sum_cost = 0   # cummulative cost
        for edge in edges:
            sum_weight += self.vertices[edge[0]].get_weight(self.vertices[edge[1]])
            sum_cost += self.vertices[edge[0]].get_cost(self.vertices[edge[1]])
        ratio = sum_weight/sum_cost  # cost ratio
        return ratio, edges

class WeightedCostedDirectedGraph(WeightedDirectedGraph):
    ''' a weighted, costed, directed graph 
    + Implement this class using inheritance.
    '''

    def __init__(self, vertex_nums:[int], edges_to_add:[(int,int, int, int)] = []):
        #TODO:  implement the constructor, taking a list of vertex id numbers
        #       and an optional list of edges.  An edge starts at the vertex
        #       identified by tuple[0], ends at the vertex identified by tuple[1],
        #       and has  weight identified by tuple[2] and cost identified by tuple[3]
        WeightedDirectedGraph.__init__(self, vertex_nums, edges_to_add)
        for item in edges_to_add:
            self.vertices[item[0]].set_cost(self.vertices[item[1]], item[3])

    def add_edge(self, source: int, dest: int, weight: int, cost: int)->None:
        '''
        add_edge() connects the source and the destination vertices
        '''
        #TODO:  implement the add_edge() function, adding a directed edge
        #       from the source vertex to the destination vertex with
        #       the specified weight and cost
        self.vertices[source].add_edge(self.vertices[dest], weight)
        self.vertices[source].set_cost(self.vertices[dest], cost)

    def calculate_fewest_edges_path(self, source: int, dest: int)-> (float, [(int, int)]):
        '''
        + calculate_fewest_edges_path() calculates the shortest path between two
        vertices in the graph.
        + The shortest path is the path with the fewest number of edges
        traversed from the source to the destination.
        + If there are multiple such paths, any one can be returned.
        + The return values are (cost ratio, [list of edges]).
        + The cost ratio is the total weight accumulated when
        traversing the identified path divided by the total cost accumulated when
        traversing the identified path:
        cost ratio = (cummulative weight) / (cummulative cost)
        + The list of edges is a list of tuples containing the vertex ids on the path
        from the source to the destination.  The list should be in the order that
        the edges are traversed along the path from the source to the destination.
        Each tuple should be ordered (source, dest) to show the direction of
        traversal.
        + If no path connects the source and destination, the function
        returns (-1, []).
        + NOTE:  an edge can only be traversed in one direction, because this is a directed graph.
        '''
        #TODO:  implement the calculate_fewest_edges_path() function.
        weight, edges = WeightedDirectedGraph.calculate_fewest_edges_path(self, source, dest)
        if weight == -1:
            # no path exist
            return -1, []
        sum_weight = 0 # cummulative weight
        sum_cost = 0   # cummulative cost
        for edge in edges:
            sum_weight += self.vertices[edge[0]].get_weight(self.vertices[edge[1]])
            sum_cost += self.vertices[edge[0]].get_cost(self.vertices[edge[1]])
        ratio = sum_weight/sum_cost
        return ratio, edges

if __name__ == "__main__":
    g1 = WeightedCostedDirectedGraph([1,2,3,4,5], 
        [(1,2,2,1), (2,5,2,1), (1,3,4,4), (3,4,2,2), (4,5,1,1)])
    print(g1.calculate_fewest_edges_path(1,4))  
    g2 = WeightedCostedUndirectedGraph([1,2,3,4,5], 
        [(1,2,2,1), (2,5,2,1), (1,3,4,4), (3,4,2,2), (4,5,1,1)])
    print(g2.calculate_fewest_edges_path(1,4))  
