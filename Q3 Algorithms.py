import collections

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = collections.defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance

         

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]  # Corrected line
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

def main():
    graph = Graph()
    graph.nodes = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'}
    graph.edges = {'A': ['B', 'C', 'D'], 'B': ['H', 'F', 'C'],
                   'C': ['B', 'F', 'E', 'D'], 'D': ['C', 'E', 'I'],
                   'E': ['D', 'C', 'F', 'G'], 'F': ['C', 'B', 'H', 'G', 'E'],
                   'G': ['E', 'F', 'H', 'I'], 'H': ['B', 'F', 'G', 'I'],
                   'I': ['D', 'G', 'H']}
    graph.distances = {('A', 'B'): 22, ('A', 'C'): 9, ('A', 'D'): 12,
                      ('H', 'B'): 34, ('B', 'H'): 34, ('F', 'B'): 36,
                      ('B', 'F'): 36, ('C', 'B'): 35, ('B', 'C'): 35,
                      ('F', 'E'): 18, ('E', 'F'): 18, ('G', 'F'): 39,
                      ('F', 'G'): 39, ('H', 'F'): 24, ('F', 'H'): 24,
                      ('I', 'G'): 21, ('G', 'I'): 21, ('H', 'G'): 25,
                      ('G', 'H'): 25, ('I', 'H'): 19, ('H', 'I'): 19,
                      ('F', 'C'): 42, ('C', 'F'): 42, ('E', 'C'): 65, ('C', 'E'): 65,
                      ('D', 'C'): 4, ('C', 'D'): 4, ('E', 'D'): 33, ('D', 'E'): 33,
                      ('I', 'D'): 30, ('D', 'I'): 30, ('G', 'E'): 23, ('E', 'G'): 23}

    visited, path = dijkstra(graph, 'A')
    print("Shortest Distances:", visited)
    print("Shortest Paths:", path)

if __name__ == "__main__":
    main()