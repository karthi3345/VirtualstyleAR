import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes
nodes = [
    "VirtualStyle AR",
    "Immersive AR Experience",
    "Personalized Shopping Journey",
    "Consumer Insights & Behavior Data",
    "Enhanced Customer Satisfaction & Engagement",
    "Redefines Retail & Customer Interaction"
]

# Add nodes
G.add_nodes_from(nodes)

# Define edges (connections)
edges = [
    ("VirtualStyle AR", "Immersive AR Experience"),
    ("VirtualStyle AR", "Personalized Shopping Journey"),
    ("VirtualStyle AR", "Consumer Insights & Behavior Data"),
    ("Immersive AR Experience", "Enhanced Customer Satisfaction & Engagement"),
    ("Personalized Shopping Journey", "Enhanced Customer Satisfaction & Engagement"),
    ("Consumer Insights & Behavior Data", "Enhanced Customer Satisfaction & Engagement"),
    ("Enhanced Customer Satisfaction & Engagement", "Redefines Retail & Customer Interaction")
]

# Add edges
G.add_edges_from(edges)

# Set layout
pos = nx.spring_layout(G, k=1.2, seed=42)  # positions for all nodes

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=3500, node_color="#87CEFA", edgecolors="black")

# Draw edges
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, edge_color="black", width=2)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

# Remove axes
plt.axis('off')
plt.title("VirtualStyle AR - Conclusion Diagram", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
