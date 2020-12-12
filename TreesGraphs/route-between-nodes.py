from queue import Queue

from .Graph import Graph, Vertex


def search_bfs(graph, start, end):
    if (start == end):
        return True

    visited = {start: True}

    queue = Queue()
    queue.put(start)
    while not queue.empty():
        vertex = queue.get()
        visited[vertex] = True
        for adjacent in graph.adjacent_vertices(vertex):
            if not visited.get(adjacent):
                if adjacent.element() == end.element():
                    return True
                else:
                    queue.put(adjacent)
    return False


graph = Graph(True)
vertexMap = {}
vertices = (1, 10, 9, 8, 12, 2, 3, 4, 0, 7, 6, 5, 11)
for element in vertices:
    vertexMap[element] = Vertex(element)
    graph.insert_vertex(vertexMap[element])

edges = ((4, 2), (2, 3), (3, 1), (1, 10), (10, 4), (8, 3), (9, 8),
         (0, 9), (0, 12), (0, 7), (7, 11), (11, 5), (5, 6), (6, 12), (12, 11))

for u, v in edges:
    graph.insert_edge(vertexMap[u], vertexMap[v])

print(search_bfs(graph, vertexMap[8], vertexMap[4]))
