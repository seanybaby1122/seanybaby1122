- 👋 Hi, I’m @seanybaby1122
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...
import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes with attributes
words = {
    "DATA": {"category": "Information", "numeric": [68, 65, 84, 65]},
    "AGRG": {"category": "Flipped Data", "numeric": [65, 71, 82, 71]},
    "TIME": {"category": "Temporal", "numeric": [84, 73, 77, 69]},
    "IMET": {"category": "Flipped Time", "numeric": [73, 77, 69, 84]},
    "CODE": {"category": "Programming", "numeric": [67, 79, 68, 69]},
    "EDOC": {"category": "Flipped Code", "numeric": [69, 68, 79, 67]}
}

for word, attributes in words.items():
    G.add_node(word, **attributes)

# Add transformation edges
edges = [
    ("DATA", "AGRG", "Flipping"),
    ("TIME", "IMET", "Flipping"),
    ("CODE", "EDOC", "Flipping"),
    ("DATA", "ATAD", "Letter Reversal"),
    ("TIME", "EMIT", "Letter Reversal"),
    ("CODE", "EDOC", "Letter Reversal"),
]

for u, v, transformation in edges:
    G.add_edge(u, v, transformation=transformation)

# Graph visualization
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Layout for visualization
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10)
edge_labels = {(u, v): d["transformation"] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Word Transformation Graph")
plt.show()

# Graph analysis
print("Nodes and Attributes:")
for node, attr in G.nodes(data=True):
    print(f"{node}: {attr}")

print("\nEdges and Transformations:")
for u, v, attr in G.edges(data=True):
    print(f"{u} -> {v}: {attr['transformation']}")

# Finding patterns
cycles = list(nx.simple_cycles(G))
print("\nDetected Cycles:", cycles)

pagerank = nx.pagerank(G)
print("\nPageRank (Importance of Nodes):", pagerank)

<!---
seanybaby1122/seanybaby1122 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
