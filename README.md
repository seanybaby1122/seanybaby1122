# prompt: prompt: prompt: import networkx as nx
# import networkx as nx
# prompt: import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
# from matplotlib_venn import venn2

import matplotlib.pyplot as plt
# prompt: from matplotlib_venn import venn2
# import matplotlib.pyplot as plt from matplotlib_venn import venn2
# Assuming 'data' and 'graph' are defined from the previous code

# Assuming 'data' and 'graph' are defined from the previous code

# Step 3: Analyze and visualize the graph (example: Venn diagram)
known_words = set(data["words"].keys())
generated_words = set(node for node, attr in graph.nodes(data=True) if attr.get("category") == "Generated")

venn2([known_words, generated_words], ('Known Words', 'Generated Words'))
plt.title("Known vs. Generated Words")
plt.show()


# Step 3: Analyze and visualize the graph (example: Venn diagram)
known_words = set(data["words"].keys())
generated_words = set(node for node, attr in graph.nodes(data=True) if attr.get("category") == "Generated")

venn2([known_words, generated_words], ('Known Words', 'Generated Words'))
plt.title("Known vs. Generated Words")
plt.show()
# prompt: Define your symbolic data
# # data = {
# #     "words": {
# #         "DATA": {"category": "Information", "numeric": [68, 65, 84, 65]},
# #         "AGRA": {"category": "Location", "numeric": [65, 71, 82, 65]},
# #     },
# #     "transformations": [
# #         {"from": "DATA", "to": "ATAD", "type": "Reverse"},
# #         {"from": "DATA", "to": "AGRA", "type": "Substitute"},
# #         {"from": "AGRA", "to": "EMIT", "type": "Substitute"},
# #     ],
# # }

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


## prompt: Create the directed graph
# # graph = nx.DiGraph()
# # # Add known word nodes
# # for word, metadata in data["words"].items():
# #     graph.add_node(word, **metadata)
# # # Add missing destination words as 'Generated' nodes
# # for transformation in data["transformations"]:
# #     to_word = transformation["to"]
# #     if to_word not in graph:
# #         graph.add_node(
# #             to_word,
# #             category="Generated",
# #             numeric=[ord(c) for c in to_word]
# #         )
# # # Add transformation edges
# # for transformation in data["transformations"]:
# #     graph.add_edge(
# #         transformation["from"],
# #         transformation["to"],
# #         transformation=transformation["type"]

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Sample data (replace with your actual data)
data = {
    "words": {
        "apple": {"category": "Fruit", "color": "Red"},
        "banana": {"category": "Fruit", "color": "Yellow"},
        "orange": {"category": "Fruit", "color": "Orange"},
        "grape": {"category": "Fruit", "color": "Purple"}
    },
    "transformations": [
        {"from": "apple", "to": "ApplePie", "type": "Baking"},
        {"from": "banana", "to": "BananaBread", "type": "Baking"},
        {"from": "orange", "to": "OrangeJuice", "type": "Juicing"},
        {"from": "grape", "to": "grapefruit", "type": "Mutation"}
    ]
}


# Step 2: Create the directed graph
graph = nx.DiGraph()
# Add known word nodes
for word, metadata in data["words"].items():
    graph.add_node(word, **metadata)
# Add missing destination words as 'Generated' nodes
for transformation in data["transformations"]:
    to_word = transformation["to"]
    if to_word not in graph:
        graph.add_node(
            to_word,
            category="Generated",
            numeric=[ord(c) for c in to_word]
        )
# Add transformation edges
for transformation in data["transformations"]:
    graph.add_edge(
        transformation["from"],
        transformation["to"],
        transformation=transformation["type"]
    )



# Assuming 'data' and 'graph' are defined from the previous code

# Step 3: Analyze and visualize the graph (example: Venn diagram)
known_words = set(data["words"].keys())
generated_words = set(node for node, attr in graph.nodes(data=True) if attr.get("category") == "Generated")

venn2([known_words, generated_words], ('Known Words', 'Generated Words'))
plt.title("Known vs. Generated Words")
plt.show()

#     )
# # # prompt: Detect and print cycles
# # cycles = list(nx.simple_cycles(graph))
# # print("Cycles in the graph:")
# # for cycle in cycles:
# #     print(cycle)

import networkx as nx

# ... (Your existing code for creating the graph) ...

# Detect and print cycles
try:
    cycles = list(nx.simple_cycles(graph))
    print("Cycles in the graph:")
    for cycle in cycles:
        print(cycle)
except nx.NetworkXNoCycle:
    print("No cycles found in the graph.")
# prompt: Visualize the graph
# # pos = nx.spring_layout(graph)
# # plt.figure(figsize=(10, 6))
# # nx.draw(
# #     graph, pos,
# #     with_labels=True,
# #     node_color='lightblue',
# #     edge_color='gray',
# #     node_size=2000,
# #     font_size=10
# # )
# # edge_labels = nx.get_edge_attributes(graph, 'transformation')
# # nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
# # plt.title("Symbolic Word Transformation Graph")
# # plt.show()

pos = nx.spring_layout(graph)
plt.figure(figsize=(10, 6))
nx.draw(
    graph, pos,
    with_labels=True,
    node_color='lightblue',
    edge_color='gray',
    node_size=2000,
    font_size=10
)
edge_labels = nx.get_edge_attributes(graph, 'transformation')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
plt.title("Symbolic Word Transformation Graph")
plt.show()

#  
# # prompt: Venn Diagram for shared characters
# # set1 = set("DATA")
# # set2 = set("AGRA")
# # plt.figure()
# # venn2([set1, set2], set_labels=('DATA', 'AGRA'))
# # plt.title("Shared Letters Between DATA and AGRA")
# # plt.show()
# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib_venn import venn2
# # ... (Your existing code for graph creation and visualization) ...

set1 = set("DATA")
set2 = set("AGRA")
plt.figure()
venn2([set1, set2], set_labels=('DATA', 'AGRA'))
plt.title("Shared Letters Between DATA and AGRA")
plt.show()
