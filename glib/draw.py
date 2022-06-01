import networkx as nx
import matplotlib.pyplot as plt
from numpy import arange

from .graph import Graph

def draw(graph: Graph, fig_size=(20, 10), node_color='#daa6ff', edge_color='#b755fb', font_size=18, font_color='black', font_family='JetBrains Mono', font_weight='semibold', node_size=3500):
  nodes = graph.nodes
  edges = graph.edges

  G = nx.Graph()
  
  for n in nodes:
    G.add_node(n)

  for e in edges:
    G.add_edge(e[0], e[1], weight=e[2])

  pos = nx.shell_layout(G)
  
  plt.figure(figsize=fig_size)
  nx.draw(G, pos, node_size=node_size, node_color=node_color, font_size=font_size, font_color=font_color, font_family=font_family, font_weight=font_weight, alpha=0.75)
  nx.draw_networkx_labels(G, pos, font_size=25, font_weight='semibold', font_family='JetBrains Mono')
  nx.draw_networkx_edges(G, pos, arrows=graph.directed, edge_color=edge_color, width=3, arrowstyle='->', arrowsize=10, node_size=node_size, alpha=0.5)
  nx.draw_networkx_edge_labels(G, pos=pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, font_size=font_size, font_weight=font_weight, font_family=font_family)
  plt.show()

def draw_matrix(matrix: list, graph=None, size=(20, 10), cmap='plasma'):
  labels = None

  if graph is not None: labels = graph.nodes
  else:                 labels = [str(i) for i in range(len(matrix))]

  fig, ax = plt.subplots(figsize=size)
  img = ax.imshow(matrix, cmap=cmap, interpolation='nearest')
  
  ax.set_xticks(arange(len(labels)))
  ax.set_yticks(arange(len(labels)))

  ax.set_xticklabels(labels)
  ax.set_yticklabels(labels)

  fig.colorbar(img, ax=ax)
  plt.show()

def draw_adj_matrix(G: Graph, size=(20, 10), cmap='plasma'):
  draw_matrix(G.M, G, size, cmap)
