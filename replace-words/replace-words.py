class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = node.children.setdefault(c, TrieNode())
                node = node.children[c]
            node.is_end = True
        
        def find_prefix(word):
            node = self.root
            for i, c in enumerate(word):
                if c not in node.children:
                    return word[:i] if node.is_end else ""
                if node.is_end: return word[:i]
                node = node.children[c]
        word_list = sentence.split(" ")
        res = []
        for w in word_list:
            prefix = find_prefix(w)
            if prefix:
                res.append(prefix)
            else:
                res.append(w)
        return " ".join(res)