class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for i in word:
            if i not in temp.children:
                temp.children[i] = TrieNode()
            temp = temp.children[i]
        temp.is_end = True
        

    def search(self, word: str) -> bool:
        temp = self.root
        for i in word:
            if temp.children[i]:
                if temp.is_end:
                    return False 
                temp = temp.children[i]
            else:
                return False
        
        if not temp.is_end:
            return False
        
        return True
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        tt = Trie()

        for i in folder:
            tt.insert(i.split("/")[1:])
        
        ans = []

        for i in folder:
            if tt.search(i.split("/")[1:]):
                ans.append(i)
        
        return ans


        