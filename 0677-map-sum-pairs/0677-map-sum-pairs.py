class TrieNode:
# Trie node class
    def __init__(self):
        self.children = [None for _ in range(26)]

        # is_end is True if node represent the end of the word
        self.is_end = False
        self.sum = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.words = defaultdict(int)
        

    def insert(self, key: str, val: int) -> None:

        temp = val
        if key in self.words:
            temp = val - self.words[key]
        
        self.words[key] = val

        current = self.root

        for ch in key:
            idx = ord(ch) - ord('a')
            if not current.children[idx]:
                current.children[idx] = TrieNode()

            current = current.children[idx]
            current.sum += temp


        current.is_end = True


    def sum(self, prefix: str) -> int:

        current = self.root

        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not current.children[idx]:
                return 0

            current = current.children[idx]


        return current.sum
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)