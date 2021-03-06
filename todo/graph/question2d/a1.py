import sys
import heapq

class PriorityQueue:
    """
      Implements a priority queue data structure.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0
        self.items = []

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.items.append(item)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        self.items.remove(item)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def __contains__(self, item):
        return item in self.items

    def update(self, item, priority):
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)



class Graph:
    def __init__(self, vertices, edges):
        self.vertices =  vertices
        self.edges = {}
        self.weights = {}
        for vertex in vertices:
            self.edges[vertex] = []
        for edge in edges:
            self.edges[edge[0]].append(edge[1])
            self.edges[edge[1]].append(edge[0])
            self.weights[(min(edge[0], edge[1]),max(edge[0], edge[1]))] = edge[2]

    def neighbors(self, node):
        return self.edges[node]

    def get_nodes(self):
        return self.vertices


    def get_cost(self, from_node, to_node):
        key = (min(from_node, to_node), max(from_node, to_node))
        return self.weights[key]

def read_file():
    # Read in the number of vertices (n) and edges (m)
    edges, queries = [], []
    vertices =set()
    n = int(input())
    m = int(input())
    
    # Read the edges from stdin.
    for _ in range(m):
        arr = input().split()
        start = int(arr[0])
        end = int(arr[1])
        vertices.add(start)
        vertices.add(end)
        cost = float(arr[2])
        edges.append((start, end, cost))
    
    # Read the A edges. You may want to use a different data-structure.
    q = int(input())
    for i in range(q):
        arr = input().split()
        v = int(arr[0])
        w = int(arr[1])
        queries.append((min(v,w), max(v,w)))

    return vertices, edges, queries


# Print the weight of the mst to two decimal-places. 

def prim_mst(graph, edges):
    marked = {}
    pq = PriorityQueue()
    mst = []
    nodes = graph.get_nodes()
    visit(graph, nodes[0], marked, pq, edges)
    while not pq.isEmpty():
        edge = pq.pop()
        v = edge[0]
        w = edge[1]
        if v in marked and w in marked:
            continue
        mst.append(edge)
        if v not in marked:
            visit(graph, v, marked,pq, edges)
        if w not in marked:
            visit(graph, w, marked, pq, edges)
    return mst

def visit(graph,v , marked, pq, edges):
    marked[v] = True
    for neighbor in graph.neighbors(v):
        edge = (min(v, neighbor), max(v, neighbor))
        cost = graph.get_cost(v, neighbor)
        if edge in edges:
            cost = 0
        if neighbor not in marked:
            pq.push(edge, cost)



if __name__ == "__main__":
    vertices, edges, queries = read_file()
    vertices = list(vertices)
    graph = Graph(vertices, edges)
    path = prim_mst(graph, queries)
    total_weight = 0
    for edge in path:
        total_weight += graph.get_cost(edge[0], edge[1])
    print("%.2f" % total_weight)