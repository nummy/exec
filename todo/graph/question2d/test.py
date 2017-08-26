import networkx as nx 
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_weighted_edges_from([(0,1,0.732),(0,3, 0.134),(0,4,0.112),(1,4,0.770),(2,5,0.379),
    (2,6, 0.984),(2,7, 0.577),(3,4,0.642),(3,6,0.763),(3,7,0.589),(4,5,0.473),(4,7,0.334),(5,6,0.748),
    (5,7,0.544),
    (6,7,0.474)])
nx.draw_networkx(G)
plt.show()