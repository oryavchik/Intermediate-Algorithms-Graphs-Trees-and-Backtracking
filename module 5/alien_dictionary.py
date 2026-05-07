"""Alien dictionary"""

def alien_order(words):
    """Function alien order"""
    adj = {}

    for word in words:
        for char in word:
            adj[char] = set()

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        min_len = min(len(word1), len(word2))

        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""

        for j in range(min_len):
            if word1[j] != word2[j]:
                adj[word1[j]].add(word2[j])
                break

    visited = {}
    order = []

    def dfs(char):
        """Function dfs"""

        if char in visited:
            return visited[char]

        visited[char] = False

        for nei in adj[char]:
            if dfs(nei) is False:
                return False

        visited[char] = True
        order.append(char)

        return True

    for char in adj:
        if char not in visited:
            if dfs(char) is False:
                return ""

    return "".join(order[::-1])
