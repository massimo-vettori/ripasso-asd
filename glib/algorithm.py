from .graph import Graph, INF

def __find(parent, i):
  if parent[i] == i:
    return i
  return __find(parent, parent[i])

def __union(parent, rank, x, y):
  xroot = __find(parent, x)
  yroot = __find(parent, y)

  if rank[xroot] < rank[yroot]:
    parent[xroot] = yroot
  elif rank[xroot] > rank[yroot]:
    parent[yroot] = xroot
  else:
    parent[yroot] = xroot
    rank[xroot] += 1

def __relax(u, v, w, d, p):
  if d[v] > d[u] + w:
    d[v] = d[u] + w
    p[v] = u



def kruskal(graph: Graph) -> Graph:
  result = Graph(directed=graph.directed) # Crea un grafo senza archi
  result.add_nodes(graph.nodes)

  i, e = 0, 0 

  nodes  = graph.nodes
  edges  = sorted(graph.edges, key=lambda x: x[2])
  parent = []
  rank   = []

  # Inizializzazione
  for node in range(len(nodes)): 
    parent.append(node)
    rank.append(0)

  # Fino a che non ho esaminato tutti gli archi
  while e < len(nodes) - 1 and i < len(edges):
    u, v, w = edges[i]
    i += 1

    x = __find(parent, nodes.index(u))
    y = __find(parent, nodes.index(v))

    if x != y:
      e += 1
      result.add_edge(u, v, w)
      __union(parent, rank, x, y)

  return result

def prim(graph: Graph) -> Graph:
  nodes  = graph.nodes
  matrix = graph.M

  selected    = [False for _ in range(len(nodes))]
  tmp         = 0
  selected[0] = True

  result = Graph(directed=graph.directed)

  while tmp < len(nodes) - 1:
    minimum = INF
    x = 0
    y = 0

    for i in range(len(nodes)):
      if selected[i]:
        for j in range(len(nodes)):
          if not selected[j] and matrix[i][j] < minimum and matrix[i][j] != 0:
            minimum = matrix[i][j]
            x = i
            y = j

    result.add_edge(nodes[x], nodes[y], matrix[x][y])
    selected[y] = True
    tmp += 1

  return result


def dijkstra(graph: Graph, src: str) -> tuple:
  from queue import PriorityQueue

  # initSS - Inizializza il vettore dei predecessori e delle distanze
  D = {n: INF  for n in graph.nodes}
  P = {n: None for n in graph.nodes}
  V = []

  D[src], P[src] = 0, None

  # Inizializzo la coda di priorità, per i nodi
  Q = PriorityQueue()
  Q.put((0, src))

  # Fino a che la coda non è vuota
  while not Q.empty():
    (_, u) = Q.get() # Estraggo il prossimo nodo da processare
    V.append(u)      # Lo aggiungo alla lista dei nodi visitati

    # Per ogni arco del nodo estratto
    for v in graph.neighbors(u):

      # Il peso dell'arco fra u e v
      w = graph.M[graph.nodes.index(u)][graph.nodes.index(v)]

      # Se il nodo ancora non è stato visitato
      if v not in V:
        __relax(u, v, w, D, P) # Aggiorno le distanze e i predecessori
        Q.put((D[v], v))     # Aggiungo il nodo alla coda

  return D, P

def bellman_ford(graph: Graph, src: str):

  # InitSS - Inizializza il vettore dei predecessori e delle distanze
  D = {n: INF for n in graph.nodes}
  P = {n: None for n in graph.nodes}
  D[src] = 0

  edges = graph.edges # Lista di tutti gli archi

  # Per ogni arco, lancia una relax tante volte quanti sono i nodi
  for _ in graph.nodes:
    for u, v, w in edges:
      __relax(u, v, w, D, P)

  # Controllo se ci sono cicli negativi
  for u, v, w in edges:
    if D[v] > D[u] + w:
      return False, D, P

  return True, D, P

def floyd_warshall(graph: Graph):
  from copy import deepcopy

  matrix = deepcopy(graph.M) # Copia la matrice del grafo
  nodes  = len(graph.nodes)  # Numero di nodi

  for k in range(nodes):
    for i in range(nodes):
      for j in range(nodes):
        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

  return matrix