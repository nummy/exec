#DO NOT change anything in this file
import random

class Vertex():
    UNCOLORED = 0
    COLOR_RED = random.choice(range(1,12,2))
    COLOR_BLUE = random.choice(range(2,12,2))

    def __init__(self, num:int, color:int = UNCOLORED):
        self._num = num
        self._edges = set()
        self._color = color
        self._visited = 0
        self._weights = {}
        self._costs = {}

    #Getters
    def get_num(self)->int:
        return self._num

    def get_neighbors(self)->list:
        return list(self._edges)

    def get_color(self)->int:
        return self._color

    def is_visited(self)->bool:
        return self._visited > 0

    def get_weight(self, other:'Vertex'):
        return self._weights[other]

    def get_cost(self, other:'Vertex'):
        return self._costs[other]

    #Setters
    def add_edge(self, other:'Vertex', weight:int)->None:
        if type(other) != Vertex:
            raise TypeError("cannot add edge between Vertex and type '{}'".format(type(other)))
        self._edges.add(other)
        self._weights[other] = weight

    def remove_edge(self, other:'Vertex')->None:
        if type(other) != Vertex:
            raise TypeError("remove_edge() on non-Vertex type '{}'".format(type(other)))
        self._edges.remove(other)
        
    def set_edges(self, neighbors:list)->None:
        if type(neighbors) != list or any([type(s) != Vertex for s in neighbors]):
            raise TypeError("invalid list of Vertices {}".format(neighbors))
        self._edges = set(neighbors)

    def set_color(self, color:int)->None:
        if not color in {Vertex.UNCOLORED, Vertex.COLOR_RED, Vertex.COLOR_BLUE}:
            raise ValueError("invalid color for Vertex: '{}'".format(color))
        self._color = color

    def set_cost(self, other:'Vertex', cost:int)->None:
        if type(other) != Vertex:
            raise TypeError("set_cost() on non-Vertex type '{}'".format(type(other)))
        if cost < 1:
            raise ValueError("cost must be at least 1: '{}'".format(cost))
        if other not in self._edges:
            raise ValueError("no edge from vertex '{}' to vertex '{}'".format(self.get_num(), other.get_num()))
        self._costs[other] = cost

    def visit(self):
        self._visited += 1

    def reset(self):
        self._visited = 0
    
    #functions for printing
    def _show_color(self)->str:
        color = "Vertex."
        if self._color == Vertex.UNCOLORED:
            color += "UNCOLORED"
        if self._color == Vertex.COLOR_RED:
            color += "RED"
        if self._color == Vertex.COLOR_BLUE:
            color += "BLUE"
        return color

    def __str__(self)->str:
        return "Vertex({num}, {color}, {edges})".format(num = self._num, color = self._show_color(), 
                edges = ["Vertex({n}, {c})".format(n = x.get_num(), c = x._show_color()) for x in self._edges])
    
if __name__ == "__main__":
    x = Vertex(1)
    y = Vertex(2)
    x.add_edge(y, -1)
    y.set_color(Vertex.COLOR_BLUE)
    z = Vertex(3)
    print(x)
