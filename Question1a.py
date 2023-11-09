# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

# An iterative DFS implementation 
# 
# -GRAPH: a dictionary of vertex and adjancent list
# -START: starting vertex for traversal
# -VISITED: a set of visited vertices 
#
def _dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        #print('The stack is:', stack)
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    p =[]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            p.append(vertex)
            queue.extend(graph[vertex] - visited)
    return p

def main():
    graph = {'A': set(['B', 'E', 'F']),
         'B': set(['A', 'C', 'F']),
         'C': set([ 'B', 'D', 'G']),
         'D': set([ 'C', 'G']),
         'E': set(['A', 'F', 'I']),
         'F': set([ 'A', 'B', 'E', 'I']),
         'G': set([ 'C', 'D']),
         'H': set([ 'K', 'L']),
         'I': set([ 'E', 'F','J', 'M']),
         'J': set([ 'G', 'I']),
         'K': set([ 'H', 'L', 'O']),
         'L': set([ 'H', 'K', 'P']),
         'M': set([ 'I', 'N']),
         'N': set([ 'M']),
         'O': set([ 'K']),
         'P' :set([ 'L'])}

    v = bfs(graph, 'A')
    print('BFS:', v)   

    v = _dfs(graph, 'A')
    print('DFS:' ,v)
    

if __name__ == '__main__':
    main()
