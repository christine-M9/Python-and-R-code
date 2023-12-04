import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

# Creating a graph for the public transport network
transport_network = nx.Graph()

# Defining lines and stations
lines = ['Red', 'Blue', 'Green', 'Orange', 'Purple']
stations_on_each_line = 5

# Adding stations and edges to represent the transport network
for line in lines:
    station_naming = [f"{line} Station {i}" for i in range(1, stations_on_each_line + 1)]
    transport_network.add_nodes_from(station_naming)
    transport_network.add_edges_from([(station_naming[i], station_naming[i + 1]) for i in range(stations_on_each_line - 1)])

# Ensuring complete interconnectivity of the network
transport_network = nx.complete_graph(transport_network)

# Visualizing the network with different colors for each line
appearance = nx.spring_layout(transport_network)

# Geting a color palette with the same number of colors as lines for good visualization.
line_palette = sns.color_palette("husl", n_colors=len(lines))

# Assigning colors to nodes based on the line they belong to
node_colors = [line_palette[lines.index(node.split(' ')[0])] for node in transport_network.nodes]


nx.draw(transport_network, appearance, node_color=node_colors, with_labels=True)

# Seting up and displaying attributes for edges representing distances
distance_info = {'Red Line': 3, 'Blue Line': 5, 'Green Line': 2, 'Orange Line': 4, 'Purple Line': 6}
distances = {(edge[0], edge[1]): value for edge, value in distance_info.items()}
nx.set_edge_attributes(transport_network, distances, 'distance')

# Visualizing names of lines and stations on the generated map
label_info = nx.get_edge_attributes(transport_network, 'distance')
nx.draw_networkx_edge_labels(transport_network, appearance, edge_labels=label_info)
plt.show()

# Transport network improvements.

# - Exploring the possibility of adding express lines that connect key stations on different lines, allowing passengers to travel between distant locations without multiple transfers.
# - Improving interchange facilities at major transfer points by providing better signage, amenities, and streamlined connections between lines.

# Saving the network plot to PDF
plt.savefig('transport_network.pdf')

# Confirming that the figure is saved using print statement(for python).
print("The transit network plot has been saved as transport_network.pdf.")
