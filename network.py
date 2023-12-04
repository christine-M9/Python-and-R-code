import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

# Creating a graph for the public transport network
transit_network = nx.Graph()

# Defining lines and stations
lines = ['Red', 'Blue', 'Green', 'Orange', 'Purple']
stations_on_each_line = 5

# Adding stations and edges to represent the transport network
for line in lines:
    station_names = [f"{line} Station {i}" for i in range(1, stations_on_each_line + 1)]
    transit_network.add_nodes_from(station_names)
    transit_network.add_edges_from([(station_names[i], station_names[i + 1]) for i in range(stations_on_each_line - 1)])

# Ensuring complete interconnectivity of the network
transit_network = nx.complete_graph(transit_network)

# Visualizing the network with different colors for each line
layout = nx.spring_layout(transit_network)

# Geting a color palette with the same number of colors as lines
line_palette = sns.color_palette("husl", n_colors=len(lines))

# Assigning colors to nodes based on the line they belong to
node_colors = [line_palette[lines.index(node.split(' ')[0])] for node in transit_network.nodes]


nx.draw(transit_network, layout, node_color=node_colors, with_labels=True)

# Seting up and displaying attributes for edges representing distances
distance_info = {'Red Line': 3, 'Blue Line': 5, 'Green Line': 2, 'Orange Line': 4, 'Purple Line': 6}
distances = {(edge[0], edge[1]): value for edge, value in distance_info.items()}
nx.set_edge_attributes(transit_network, distances, 'distance')

# Visualizing names of lines and stations on the generated map
label_info = nx.get_edge_attributes(transit_network, 'distance')
nx.draw_networkx_edge_labels(transit_network, layout, edge_labels=label_info)
plt.show()

# Suggestions in transport network improvements.

# - Explore the possibility of adding express lines.
# - Evaluate transfer points for potential commuter experience improvements.

# Saving the network plot to PDF
plt.savefig('transport_network.pdf')

# Confirm that the figure is saved.
print("The transit network plot has been saved as transport_network.pdf.")
