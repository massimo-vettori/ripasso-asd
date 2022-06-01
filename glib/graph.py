INF = float('inf')


class Graph:
  @staticmethod
  def createDenseGraph(nodes: list, directed: bool = False, no_self_edges: bool = True):
    from random import randint

    g = Graph(directed=directed, no_self_edges=no_self_edges)
    g.add_nodes(nodes)
    for i in range(len(nodes)):
      for j in range(len(nodes)):
        g.add_edge(nodes[i], nodes[j], randint(1, 100))
    return g

  @staticmethod
  def createRandomGraph(nodes: list, directed: bool = False, no_self_edges: bool = True):
    from random import randint

    g = Graph(directed=directed, no_self_edges=no_self_edges)
    g.add_nodes(nodes)

    for i in range(len(nodes)):
      for j in range(len(nodes)):
        if randint(0, 1) == 1:
          g.add_edge(nodes[i], nodes[j], randint(1, 100))

    return g


  def __init__(self, nodes=None, directed=False, no_self_edges=True):
    self.V = [] # Lista dei nodi
    self.M = [] # Matrice di adiacenza
    self.directed = directed # True se il grafo è orientato, False altrimenti
    self.no_self_edges = no_self_edges # True se non è permesso inserire un arco da un nodo a se stesso
    self.add_nodes(nodes or []) # Se nodes è None, creo un grafo vuoto, altrimenti lo inizializzo con i nodi passati

  def add_node(self, node: str):
    if node not in self.V:
      self.M.append([INF] * len(self.V)) # Creo una riga di INF
      self.V.append(node)                # Aggiungo il nodo
      for row in self.M:
        row.append(INF)                  # Aggiungo una colonna di INF

      self.M[-1][-1] = 0                 # Il nodo aggiunto ha come distanza da se stesso 0

  def add_nodes(self, nodes: list):
    for node in nodes:
      self.add_node(node)

  def remove_node(self, node: str):
    if node in self.V:
      index = self.V.index(node)
      del self.V[index] # Rimuovo il nodo
      del self.M[index] # Rimuovo la riga del nodo
      for row in self.M:
        del row[index]  # Rimuovo la colonna del nodo

  def add_edge(self, a: str, b: str, weight: int = 1):
    if a not in self.V: self.add_node(a) # Se il nodo non esiste lo aggiungo
    if b not in self.V: self.add_node(b) # Se il nodo non esiste lo aggiungo

    row = self.V.index(a) # Indice della riga del nodo a nella matrice di adiacenza
    col = self.V.index(b) # Indice della colonna del nodo b nella matrice di adiacenza

    if row == col and self.no_self_edges: return # Evito di inserire un arco da un nodo a se stesso se non è permesso

    self.M[row][col] = weight # Aggiungo l'arco
    if not self.directed and row != col:
      self.M[col][row] = weight # Aggiungo l'arco in direzione opposta se il grafo non è orientato

  def parse_edge(self, edge: str):
    """
    Traduce una stringa "a b w" in un arco (a, b, w)
    NOTA: edge deve essere una stringa formata da 3 parti separata da spazi, se non lo è lancia un errore
    """

    try:
      a, b, w = edge.split(' ') # Separo i nodi e il peso dell'arco
      self.add_edge(a, b, int(w)) # Aggiungo l'arco
    except:
      raise ValueError('Invalid edge format, must be "a b w", but got: "' + edge + '"')

  def parse_edges(self, edges: list):
    for edge in edges:
      self.parse_edge(edge)

  def remove_edge(self, a: str, b: str):
    if a in self.V and b in self.V:
      row = self.V.index(a)
      col = self.V.index(b)

      self.M[row][col] = INF if row != col else 0
      if not self.directed:
        self.M[col][row] = INF if row != col else 0

  def neighbors(self, node: str):
    if node in self.V:
      row = self.V.index(node)
      return [self.V[i] for i in range(len(self.V)) if (self.M[row][i] != INF) and ((self.M[row][i] != 0 and row == i and not self.no_self_edges) or (row != i))] # Lista dei nodi adiacenti

    return []

  @property
  def nodes(self):
    return self.V

  @property
  def edges(self) -> list:
    return [(self.V[i], self.V[j], self.M[i][j]) for i in range(len(self.V)) for j in range(len(self.V)) if (self.M[i][j] != INF) and (i != j or (not self.no_self_edges and self.M[i][j] != 0))]
  
  @property
  def adjacency_matrix(self):
    from copy import deepcopy
    return deepcopy(self.M)
