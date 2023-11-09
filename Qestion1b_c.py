''' The modified script is contributed by Maarten Fabre available at
https://codereview.stackexchange.com/questions/193410/breadth-first-search-implementation-in-python-3-to-find-path-between-two-given-n
'''

def bfs_path(graph, start, goal):
    """
    finds a shortest path in undirected `graph` between `start` and `goal`. 
    If no path is found, returns `None`
    """
    if start == goal:
        return [start]
    visited = {start}
    queue = [(start, [])]

    while queue:
        current, path = queue.pop(0) 
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor == goal:
                return path + [current, neighbor]
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            visited.add(neighbor)   
    return None 

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))


def main():
    graph = {
        'A': set(['B', 'E', 'F']),
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
             'P' :set([ 'L'])
    }
    
    v = dfs_path(graph, 'A', 'M')
    print ('DFS path is:' ,v)
    
    path = bfs_path(graph, 'A', 'M')
    if path:
        print('BFS pathi s:' ,path)
    else:
        print('no path found')
        
        
if __name__ == '__main__':
    main()

