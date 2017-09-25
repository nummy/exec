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

    #Getters
    def get_num(self)->int:
        return self._num

    def get_neighbors(self)->list:
        return list(self._edges)

    def get_color(self)->int:
        return self._color

    def is_visited(self)->bool:
        return self._visited > 0

    #Setters
    def add_edge(self, other:'Vertex')->None:
        if type(other) != Vertex:
            raise TypeError("cannot add edge between Vertex and type '{}'".format(type(other)))
        self._edges.add(other)

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
    x.add_edge(y)
    y.set_color(Vertex.COLOR_BLUE)
    print(x)
