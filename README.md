# prompt: prompt: prompt: import networkx as nx
# import networkx as nx
# prompt: import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
# from matplotlib_venn import venn2

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Assuming 'data' and 'graph' are defined from the previous code

# Step 3: Analyze and visualize the graph (example: Venn diagram)
known_words = set(data["words"].keys())
generated_words = set(node for node, attr in graph.nodes(data=True) if attr.get("category") == "Generated")

venn2([known_words, generated_words], ('Known Words', 'Generated Words'))
plt.title("Known vs. Generated Words")
plt.show()

# # Step 1: Define your symbolic data
# data = {
#     "words": {
#         "DATA": {"category": "Information", "numeric": [68, 65, 84, 65]},
#         "AGRA": {"category": "Location", "numeric": [65, 71, 82, 65]},
#     },
#     "transformations": [
#         {"from": "DATA", "to": "ATAD", "type": "Reverse"},
#         {"from": "DATA", "to": "AGRA", "type": "Substitute"},
#         {"from": "AGRA", "to": "EMIT", "type": "Substitute"},
#     ],
# }
# # Step 2: Create the directed graph
# graph = nx.DiGraph()
# # Add known word nodes
# for word, metadata in data["words"].items():
#     graph.add_node(word, **metadata)
# # Add missing destination words as 'Generated' nodes
# for transformation in data["transformations"]:
#     to_word = transformation["to"]
#     if to_word not in graph:
#         graph.add_node(
#             to_word,
#             category="Generated",
#             numeric=[ord(c) for c in to_word]
#         )
# # Add transformation edges
# for transformation in data["transformations"]:
#     graph.add_edge(
#         transformation["from"],
#         transformation["to"],
#         transformation=transformation["type"]
#     )
# # Step 3: Detect and print cycles
# cycles = list(nx.simple_cycles(graph))
# print("Cycles in the graph:")
# for cycle in cycles:
#     print(cycle)
# # Step 4: Visualize the graph
# pos = nx.spring_layout(graph)
# plt.figure(figsize=(10, 6))
# nx.draw(
#     graph, pos,
#     with_labels=True,
#     node_color='lightblue',
#     edge_color='gray',
#     node_size=2000,
#     font_size=10
# )
# edge_labels = nx.get_edge_attributes(graph, 'transformation')
# nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
# plt.title("Symbolic Word Transformation Graph")
# plt.show()
# # Step 5 (Optional): Venn Diagram for shared characters
# set1 = set("DATA")
# set2 = set("AGRA")
# plt.figure()
# venn2([set1, set2], set_labels=('DATA', 'AGRA'))
# plt.title("Shared Letters Between DATA and AGRA")
# plt.show()

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# ... (Your existing code for graph creation and visualization) ...


