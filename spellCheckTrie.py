# CAT
# COW
# DOG


#       ROOT
#    C        D
#   A O        O
#   T W         G

class TrieNode:
    def __init__(self):
        self.children ={}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for ch in word.lower():
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True
    def search(self,word):
            curr = self.root
            for ch in word.lower():
                if ch not in curr.children:
                    return False
                curr = curr.children[ch]
            return curr.is_end 

tr = Trie()
tr.insert("cat")
tr.insert("car")
tr.insert("cab")
tr.insert("Dog")
tr.insert("Dom")


print(tr.search("can"))
print(tr.search("car"))