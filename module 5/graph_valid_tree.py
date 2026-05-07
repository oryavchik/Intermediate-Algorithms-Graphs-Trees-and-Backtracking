"""Graph valid tree"""

def valid_tree(n, edges):
    """Function valid tree"""

    if len(edges) != n - 1:
        return False

    graph = {}
    for i in range(n):
        graph[i] = []

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        """Function dfs"""

        if node in visited:
            return False

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            path_clear = dfs(neighbor, node)
            if path_clear is False:
                return False

        return True

    return dfs(0, -1) and len(visited) == n
