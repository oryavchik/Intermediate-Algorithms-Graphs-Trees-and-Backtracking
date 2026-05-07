"""Course schedule"""

def can_finish(n, prerequisites):
    """Function can finish"""
    graph = []

    for _ in range(n):
        graph.append([])

    cycle = [False] * n

    for pair in prerequisites:
        graph[pair[0]].append(pair[1])

    def dfs(course):
        """Function dfs"""
        if cycle[course]:
            return False

        if graph[course] == []:
            return True

        cycle[course] = True

        for prereq in graph[course]:
            if dfs(prereq) is False:
                return False

        cycle[course] = False
        graph[course] = []
        return True

    for i in range(n):
        if dfs(i) is False:
            return False

    return True
