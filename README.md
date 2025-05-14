# prompt: You’ve made great progress modeling symbolic word transformations as a directed graph. Let’s address a few issues and elevate the code for correctness, completeness, and visualization:
# ⸻
# 1. Fix: print(cycle) is missing
# Currently, your loop ends with cycle, which doesn’t display anything. Replace it with print(cycle):
# print("Cycles in the graph:")
# for cycle in cycles:
#     print(cycle)
# ⸻
# 2. Fix: Add missing reversed words to the graph
# The transformation list includes "ATAD", "EMIT", which aren’t defined in the words dictionary. You need to add them to the node set before building edges:
# # Automatically add missing destination words with default metadata
# for transformation in data["transformations"]:
#     to_word = transformation["to"]
#     if to_word not in graph:
#         graph.add_node(to_word, category="Generated", numeric=[ord(c) for c in to_word])
# ⸻
# 3. Bonus: Draw the transformation graph
# You can visualize it with labels to see symbolic transformations clearly:
# pos = nx.spring_layout(graph)
# plt.figure(figsize=(10, 6))
# nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
# # Draw edge labels (transformation types)
# edge_labels = nx.get_edge_attributes(graph, 'transformation')
# nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
# plt.title("Symbolic Word Transformation Graph")
# plt.show()
# ⸻
# 4. Optional: Venn Diagram of Shared Characters
# You mentioned matplotlib-venn—here’s a quick example for showing overlap in letter sets between any two words (e.g. "DATA" and "AGRG"):
# from matplotlib_venn import venn2
# set1 = set("DATA")
# set2 = set("AGRG")
# venn2([set1, set2], set_labels=('DATA', 'AGRG'))
# plt.title("Shared Letters Between DATA and AGRG")
# plt.show()
# ⸻
# Cleaned-Up Version Summary
# Here’s a full cleaned version of your code:
# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib_venn import venn2
# data = {
#     "words": {
#         "DATA": {"category": "Information", "n

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

data = {
    "words": {
        "DATA": {"category": "Information", "numeric": [68, 65, 84, 65]},
        "AGRA": {"category": "Location", "numeric": [65, 71, 82, 65]},
    },
    "transformations": [
        {"from": "DATA", "to": "ATAD", "type": "Reverse"},
        {"from": "DATA", "to": "AGRA", "type": "Substitute"},
        {"from": "AGRA", "to": "EMIT", "type": "Substitute"},
    ],
}

graph = nx.DiGraph()

# Add words as nodes with their metadata
for word, metadata in data["words"].items():
    graph.add_node(word, **metadata)

# Automatically add missing destination words with default metadata
for transformation in data["transformations"]:
    to_word = transformation["to"]
    if to_word not in graph:
        graph.add_node(to_word, category="Generated", numeric=[ord(c) for c in to_word])

# Add transformations as edges
for transformation in data["transformations"]:
    graph.add_edge(transformation["from"], transformation["to"], transformation=transformation["type"])

# Find cycles in the graph
cycles = list(nx.simple_cycles(graph))

print("Cycles in the graph:")
for cycle in cycles:
    print(cycle)

# Draw the graph
pos = nx.spring_layout(graph)
plt.figure(figsize=(10, 6))
nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)

# Draw edge labels (transformation types)
edge_labels = nx.get_edge_attributes(graph, 'transformation')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

plt.title("Symbolic Word Transformation Graph")
plt.show()

# Example Venn Diagram
set1 = set("DATA")
set2 = set("AGRA")
plt.figure()
venn2([set1, set2], set_labels=('DATA', 'AGRA'))
plt.title("Shared Letters Between DATA and AGRA")
plt.show()


