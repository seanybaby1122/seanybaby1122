# Word Transformation Graph with JSON

This project leverages graph theory to explore word transformations and represents these transformations using JSON. The words and their attributes, including categories and numeric representations, are stored in JSON format. These words and their transformations are visualized as a directed graph, allowing you to analyze relationships and transformations like flipping or letter reversal.

## Key Features

- Word transformations are represented as a directed graph.
- Words and their attributes (category, numeric values) are stored in a JSON file.
- Supports transformations like "Flipping" and "Letter Reversal" between words.
- Utilizes NetworkX for graph creation and Matplotlib for visualization.
- Performs graph analysis, including detecting cycles and calculating PageRank.

## Installation

To run this project, make sure you have Python 3.6+ and the following libraries installed:

- `networkx` for graph manipulation.
- `matplotlib` for graph visualization.
- `json` for working with JSON files (Python’s built-in library).

You can install the necessary libraries with pip:

```bash
pip install networkx matplotlib
{
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
git clone https://github.com/seanybaby1122/word-transformation-graph.git
cd word-transformation-graph
# Detect cycles in the graph
cycles = list(nx.simple_cycles(G))
print("Detected Cycles:", cycles)

# Calculate PageRank for each node
pagerank = nx.pagerank(G)
print("PageRank (Importance of Nodes):", pagerank)
---

### Summary of Key Updates:
1. **Introduction**: Focus on using JSON for word attributes and transformations.
2. **JSON Structure**: Example of how the JSON file should look for the project (with words and transformations).
3. **Usage**: Simple guide to clone the repo, prepare the JSON file, and run the script.
4. **Graph Analysis**: Mention of basic graph analysis (cycle detection, PageRank).
5. **Contributing & License**: Encouragement for collaboration and a clear license section.

This should provide clarity on how the JSON file fits into your project and help others understand how to use and contribute to the code!
