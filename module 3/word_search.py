"""Word search using trie and dfs"""
class TrieNode:
    """class TrieNode"""
    def __init__(self):
        """Function init"""
        self.children = {}
        self.is_end = False

class Solution:
    """class Solution"""
    def build_trie(self, words):
        """Function build trie"""
        root = TrieNode()

        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

        return root

    def dfs(self, board, node, i, j, path, result):
        """Function dfs"""

        if node.is_end:
            result.add(path)
            node.is_end = False

        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or
                board[i][j] not in node.children):
            return

        temp = board[i][j]
        board[i][j] = "#"

        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            self.dfs(board, node.children[temp], x, y, path + temp, result)

        board[i][j] = temp

    def find_words(self, board: list[list[str]],
                  words: list[str]) -> list[str]:
        """Function find words"""

        root = self.build_trie(words)
        result = set()

        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value in root.children:
                    self.dfs(board, root, i, j, "", result)

        return list(result)
