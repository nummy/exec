import sys

def read_file():
    edges, queries = [], []
    vertices =set()
    n = int(input())
    m = int(input())

    for _ in range(m):
        arr = input().split()
        start = int(arr[0])
        end = int(arr[1])
        vertices.add(start)
        vertices.add(end)
        cost = float(arr[2])
        edges.append((start, end, cost))

    q = int(input())

    for _ in range(q):
        arr = input().split()
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
    if start not in graph:
        return False
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return False

def main():
    vertices, edges, queries = read_file()
    graph = build_graph(vertices, edges)
    for query in queries:
        if find_path(graph, query[0], query[1]):
            print("1")
        else:
            print("0")

main()