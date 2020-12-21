class Edge:
    def __init__(self, u, v, x):
        self._origin = u
        self._destination = v
        self._element = x

    def endpoint(self):
        return (self._origin, self._destination)

    def opposite(self, v):
        return self._destination if v is self._origin else self._origin

    def element(self):
        return (self._origin.element(), self._destination.element())

    def __hash__(self):
        return hash((self._origin, self._destination))


class Vertex:
    def __init__(self, element):
        self._element = element

    def element(self):
        return self._element

    def __hash__(self):
        return hash(id(self))


class Graph:
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum((len(self._outgoing[v] for v in self._outgoing)))

        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()  # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def adjacent_vertices(self, vertex, outgoing=True):
        for edge in self.incident_edges(vertex, outgoing):
            yield edge.opposite(vertex)

    def insert_vertex(self, x=None):
        self._outgoing[x] = {}
        if self.is_directed():
            self._incoming[x] = {}

    def insert_edge(self, u, v, x=None):
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def delete_edge(self, edge: Edge):
        del self._outgoing[edge._origin][edge._destination]
        del self._incoming[edge._destination][edge._origin]
