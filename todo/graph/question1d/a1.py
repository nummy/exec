# Read in the number of vertices (n) and edges (m)
# n = int(input())
# m = int(input())

# edges, queries = [], []

# for _ in range(m):
#     edges.append(input().split())

# q = int(input())

# for _ in range(q):
#     queries.append(input().split())
	
# Print a `1` to stdout for each query. This section should be altered to instead print a `1` where the
# query indicates a connection and `0` else.

# for _ in queries:
#     print(int(True))

from collections import deque

def read_file():
    #filename = raw_input("Please input the file name:")
    filename="graph8.in"
    edges, queries = [], []
    vertices =set()
    with open(filename, "r") as fp:
        n = int(next(fp).strip())
        m = int(next(fp).strip())
        for i in range(m):
            line = next(fp).strip()
            arr = line.split()
            start = int(arr[0])
            end = int(arr[1])
            vertices.add(start)
            vertices.add(end)
            weight = float(arr[2])
            edges.append((start, end, weight))
        q = int(next(fp).strip())
        for i in range(q):
            line = line.strip()
            arr = line.split()
            queries.append([int(arr[0]), int(arr[1])])
    return vertices, edges, queries

def build_graph(vertices, edges):
    graph = {}
    for vertex in vertices:
        graph[vertex] = []
    for edge in edges:
        start = edge[0]
        end = edge[1]
        graph[start].append(end)
        graph[end].append(start)
    return graph

def find_path(graph, start, goal):
    visited = set()
    queue = deque()
    queue = queue.appendleft(start)
    while queue:
        node = queue.pop()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.appendleft(neighbor)
    return False

def main():
    vertices, edges, queries = read_file()
    graph = build_graph(vertices, edges)
    print graph
    for query in queries:
        print find_path(graph, query[0], query[1])

main()