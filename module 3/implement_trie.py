"""Implement trie (prefix tree)"""
class TrieNode:
    """class TrieNode"""
    def __init__(self):
        """Function init"""
        self.children = {}
        self.is_end = False

class Trie:
    """class Trie"""
    def __init__(self):
        """Function init"""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Function insert"""
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        """Function search"""
        node = self.root

        for char in word:
            if char not in node.children:
                return None

            node = node.children[char]

        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Function starts with"""
        node = self.root

        for char in prefix:
            if char not in node.children:
                return None

            node = node.children[char]

        return node
