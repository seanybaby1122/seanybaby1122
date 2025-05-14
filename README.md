# Word Transformation Graph with JSON

# prompt: pip install networkx matplotlib
# {
#   "words": {
#     "DATA": {"category": "Information", "numeric": [68, 65, 84, 65]},
#     "AGRG": {"category": "Flipped Data", "numeric": [65, 71, 82, 71]},
#     "TIME": {"category": "Temporal", "numeric": [84, 73, 77, 69]},
#     "IMET": {"category": "Flipped Time", "numeric": [73, 77, 69, 84]},
#     "CODE": {"category": "Programming", "numeric": [67, 79, 68, 69]},
#     "EDOC": {"category": "Flipped Code", "numeric": [69, 68, 79, 67]}
#   },
#   "transformations": [
#     {"from": "DATA", "to": "AGRG", "transformation": "Flipping"},
#     {"from": "TIME", "to": "IMET", "transformation": "Flipping"},
#     {"from": "CODE", "to": "EDOC", "transformation": "Flipping"},
#     {"from": "DATA", "to": "ATAD", "transformation": "Letter Reversal"},
#     {"from": "TIME", "to": "EMIT", "transformation": "Letter Reversal"},
#     {"from": "CODE", "to": "EDOC", "transformation": "Letter # prompt: pip install networkx matplotlib
# # {
# #   "words": {
# #     "DATA": {"category": "Information", "numeric": [68, 65, 84, 65]},
# #     "AGRG": {"category": "Flipped Data", "numeric": [65, 71, 82, 71]},
# #     "TIME": {"category": "Temporal", "numeric": [84, 73, 77, 69]},
# #     "IMET": {"category": "Flipped Time", "numeric": [73, 77, 69, 84]},
# #     "CODE": {"category": "Programming", "numeric": [67, 79, 68, 69]},
# #     "EDOC": {"category": "Flipped Code", "numeric": [69, 68, 79, 67]}
# #   },
# #   "transformations": [
# #     {"from": "DATA", "to": "AGRG", "transformation": "Flipping"},
# #     {"from": "TIME", "to": "IMET", "transformation": "Flipping"},
# #     {"from": "CODE", "to": "EDOC", "transformation": "Flipping"},
# #     {"from": "DATA", "to": "ATAD", "transformation": "Letter Reversal"},
# #     {"from": "TIME", "to": "EMIT", "transformation": "Letter Reversal"},
# #     {"from": "CODE", "to": "EDOC", "transformation": "Letter Reversal"}
# #   ]
# # }
# # git clone https://github.com/seanybaby1122/word-transformation-graph.git
# # cd word-transformation-graph
# # # Detect cycles in the graph
# # 

import json
import networkx as nx
import matplotlib.pyplot as plt

data = {
  "words": {
    "DATA": {"category": "Information", "numeric": [68, 65, 84, 65]},
    "AGRG": {"category": "Flipped Data", "numeric": [65, 71, 82, 71]},
    "TIME": {"category": "Temporal", "numeric": [84, 73, 77, 69]},
    "IMET": {"category": "Flipped Time", "numeric": [73, 77, 69, 84]},
    "CODE": {"category": "Programming", "numeric": [67, 79, 68, 69]},
    "EDOC": {"category": "Flipped Code", "numeric": [69, 68, 79, 67]}
  },
  "transformations": [
    {"from": "DATA", "to": "AGRG", "transformation": "Flipping"},
    {"from": "TIME", "to": "IMET", "transformation": "Flipping"},
    {"from": "CODE", "to": "EDOC", "transformation": "Flipping"},
    {"from": "DATA", "to": "ATAD", "transformation": "Letter Reversal"},
    {"from": "TIME", "to": "EMIT", "transformation": "Letter Reversal"},
    {"from": "CODE", "to": "EDOC", "transformation": "Letter Reversal"}
  ]
}

graph = nx.DiGraph()

for word, attributes in data["words"].items():
  graph.add_node(word, category=attributes["category"], numeric=attributes["numeric"])

for transformation in data["transformations"]:
  graph.add_edge(transformation["from"], transformation["to"], transformation=transformation["transformation"])

cycles = list(nx.simple_cycles(graph))

print("Cycles in the graph:")
for cycle in cycles:
    print(cycle)

# Draw the graph
pos = nx.spring_layout(graph)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(graph, pos, node_size=700)

# edges
nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(), edge_color='black')

# labels
nx.draw_networkx_labels(graph, pos, font_size=10, font_family='sans-serif')
plt.axis('off')
plt.show()
