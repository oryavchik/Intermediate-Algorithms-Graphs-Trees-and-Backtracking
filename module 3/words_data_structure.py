"""Design add and search words data structure"""
class TrieNode:
    """class TrieNode"""
    def __init__(self):
        """Function init"""
        self.children = {}
        self.is_end = False

class WordDictionary:
    """class WordDictionary"""

    def __init__(self):
        """Function init"""
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        """Function add word"""
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        """Function search"""

        def dfs(node, i):
            """Function dfs"""

            if i == len(word):
                return node.is_end

            if word[i] == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False

            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)
            return False

        return dfs(self.root, 0)
