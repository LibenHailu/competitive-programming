class TrieNode:
    def __init__(self):
        self.nodes = [None] * 26
        self.is_end = False
class Trie:

    def __init__(self):
        self.root = TrieNode()      

    def insert(self, word: str) -> None:
        Node = self.root
        for c in word:
            if not Node.nodes[ord(c) - ord('a')]:
                Node.nodes[ord(c) - ord('a')] = TrieNode()
            Node = Node.nodes[ord(c) - ord('a')]
        Node.is_end = True

    def search(self, word: str) -> bool:
        Node = self.root
        for c in word:
            if not Node.nodes[ord(c) - ord('a')]:
                return False
            Node = Node.nodes[ord(c) - ord('a')]
        return Node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        Node = self.root
        for c in prefix:
            if not Node.nodes[ord(c) - ord('a')]:
                return False
            Node = Node.nodes[ord(c) - ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)