from TreesGraphs.Graph import Graph, Vertex


# TODO implement cyclic dependency support
def find_build_order(graph: Graph):
    buildOrder = []
    while len(buildOrder) != len(graph.vertices()):
        for vertex in graph.vertices():
            if vertex.element() not in buildOrder:
                incoming_edges = set()
                outgoing_edges = set()
                for x in graph.incident_edges(vertex, False):
                    incoming_edges.add(x)  # consume generator
                for x in graph.incident_edges(vertex):
                    outgoing_edges.add(x)  # consume generator
                print(vertex.element(), len(incoming_edges), buildOrder)
                if len(incoming_edges) == 0:
                    buildOrder.append(vertex.element())
                    for edge in outgoing_edges:
                        graph.delete_edge(edge)

    return buildOrder


a, b, c, d, e, f, g = Vertex('a'), Vertex('b'), Vertex(
    'c'), Vertex('d'), Vertex('e'), Vertex('f'), Vertex('g')
vertices = (a, b, c, d, e, f, g)
edges = ((f, c), (f, b), (f, a), (a, e),
         (d, g), (b, e), (c, a), (b, a), (e, c))

graph = Graph(True)

for vertex in vertices:
    graph.insert_vertex(vertex)

for u, v in edges:
    graph.insert_edge(u, v)


print(find_build_order(graph))
