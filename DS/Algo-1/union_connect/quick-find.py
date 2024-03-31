class UnionFind:
    def __init__(self, total) -> None:
        self.total = total
        self.components = list(range(0, total))

    
    def find(self, p, q):
        if self.components[p] == self.components[q]:
            return "Components are connected"
        return "Not connected"
    
    def union(self, p, q): # Time complexity is O(n^2) on N union operations
        pid = self.components[p]
        qid = self.components[q]

        for i in range(self.total):
            if self.components[i] == pid:
                self.components[i] = qid

uf = UnionFind(10)
uf.union(3, 4)
uf.union(3, 8)