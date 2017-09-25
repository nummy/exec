import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    graph = defaultdict(set)
    for line in file:
    	nodes = line.strip().split(";")
    	graph[nodes[0]].add(nodes[1])
    return graph


def graph_as_str(graph : {str:{str}}) -> str:
   	res = ""
   	for source, destinations in sorted(graph.items()):
   		res = res + ("  {source} -> [{destinations}]\n").format(source=source,destinations=", ".join(repr(x) for x in sorted(destinations)))
   	return res
        
def reachable(graph : {str:{str}}, start : str) -> {str}:
	reached_nodes = set()
	unexplored_nodes = [start]
	while len(unexplored_nodes) != 0:
		node = unexplored_nodes.pop()
		reached_nodes.add(node)
		neighs = graph.get(node, set())
		for neigh in neighs:
			if neigh not in reached_nodes:
				unexplored_nodes.append(neigh)
	return reached_nodes


if __name__ == '__main__':
	# Write script here
	file = goody.safe_open('Enter a file representing a graph','r','Illegal file name')
	graph = read_graph(file)
	print("Graph: source node -> [all destination nodes]")
	print(graph_as_str(graph))
	while True:
		start = prompt.for_string("Enter a name representing the start node (else quit)")
		if start == "quit":
			break
		while start not in graph:
			print("Entry Error: '%s';  Illegal: not a source node\nPlease enter a legal String" % start)
			start = prompt.for_char("Enter a name representing the start node (else quit)")
		reached_nodes = reachable(graph, start)
		print("From %s the reachable nodes are %s" %(start, str(reached_nodes)))
	print()
	import driver
	driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
	driver.driver()
