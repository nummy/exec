# Read in the number of vertices (n) and edges (m)
n = int(input())
m = int(input())

# Read the edges from stdin.
edges = []
for _ in range(m):
    edges.append(input().split())

# Read the A edges. You may want to use a different data-structure.
n_A, A = int(input()), []

for _ in range(n_A):
	A.append(input().split())

	
mst_weight = 0.

# Print the weight of the mst to two decimal-places. 
print('{:.2f}'.format(mst_weight))
