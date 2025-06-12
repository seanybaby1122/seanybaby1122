# prompt: # prompt: prompt: prompt: import networkx as nx
# # import networkx as nx
# # prompt: import matplotlib.pyplot as plt
# # import matplotlib.pyplot as plt
# # from matplotlib_venn import venn2
# import matplotlib.pyplot as plt
# # prompt: from matplotlib_venn import venn2
# # import matplotlib.pyplot as plt from matplotlib_venn import venn2
# # Assuming 'data' and 'graph' are defined from the previous code
# # Assuming 'data' and 'graph' are defined from the previous code
# # Step 3: Analyze and visualize the graph (example: Venn diagram)
# known_words = set(data["words"].keys())
# generated_words = set(node for node, attr in graph.nodes(data=True) if attr.get("category") == "Generated")
# venn2([known_words, generated_words], ('Known Words', 'Generated Words'))
# plt.title("Known vs. Generated Words")
# plt.show()
# # Step 3: Analyze and visualize the graph (example: Venn diagram)
# known_words = set(data["words"].keys())
# generated_words = set(node for node, attr in graph.nodes(data=True) if attr.get("category") == "Generated")
# venn2([known_words, generated_words], ('Known Words', 'Generated Words'))
# plt.title("Known vs. Generated Words")
# plt.show()
# # prompt: Define your symbolic data
# # # data = {
# # #     "words": {
# # #         "DATA": {"category": "Information", "numeric": [68, 65, 84, 65]},
# # #         "AGRA": {"category": "Location", "numeric": [65, 71, 82, 65]},
# # #     },
# # #     "transformations": [
# # #         {"from": "DATA", "to": "ATAD", "type": "Reverse"},
# # #         {"from": "DATA", "to": "AGRA", "type": "Substitute"},
# # #         {"from": "AGRA", "to": "EMIT", "type": "Substitute"},
# # #     ],
# # # }
# data = {
#     "words": {
#         "DATA": {"category": "Information", "numeric": [68, 65, 84, 65]},
#         "AGRA": {"category": "Location", "numeric": [65, 71, 82, 65]},
#     },
#     "transformations": [
#         {"from": "DATA", "to": "ATAD", "type": "Reverse"},
#         {"from": "DATA", "to": "AGRA", "type": "Substitute"},
# prompt: # prompt: prompt: import networkx as nx
# # import networkx as nx
# # prompt: import matplotlib.pyplot as plt
# # import matplotlib.pyplot as plt
# # from matplotlib_venn import venn2
# import matplotlib.pyplot as plt
# # prompt: from matplotlib_venn import venn2
# # import matplotlib.pyplot as plt from matplotlib_venn import venn2
# # Assuming 'data' and 'graph' are defined from the previous code
# # Assuming 'data' and 'graph' are defined from the previous code
# # Step 3: Analyze and visualize the graph (example: Venn diagram)
# known_words = set(data["words"].keys())
# generated_words = set(node for node, attr in graph.nodes(data=True) if attr.get("category") == "Generated")
# venn2([known_words, generated_words], ('Known Words', 'Generated Words'))
# plt.title("Known vs. Generated Words")
# plt.show()
# # Step 3: Analyze and visualize the graph (example: Venn diagram)
# known_words = set(data["words"].keys())
# generated_words = set(node for node, attr in graph.nodes(data=True) if attr.get("category") == "Generated")
# venn2([known_words, generated_words], ('Known Words', 'Generated Words'))
# plt.title("Known vs. Generated Words")
# plt.show()
# # prompt: Define your symbolic data
# # # data = {
# # #     "words": {
# # #         "DATA": {"category": "Information", "numeric": [68, 65, 84, 65]},
# # #         "AGRA": {"category": "Location", "numeric": [65, 71, 82, 65]},
# # #     },
# # #     "transformations": [
# # #         {"from": "DATA", "to": "ATAD", "type": "Reverse"},
# # #         {"from": "DATA", "to": "AGRA", "type": "Substitute"},
# # #         {"from": "AGRA", "to": "EMIT", "type": "Substitute"},
# # #     ],
# # # }
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
.github/workflows/docker-ci.yml
