import time


class UnionFind:
    def __init__(self, total) -> None:
        self.total = total
        self.components = list(range(0, total))
        self.sz = [1] *  self.total

    def traverse_roots(self, val):
        root = self.components[val]
        while root != self.components[root]:
            root = self.components[root]
        return root

    
    def find(self, p, q):
        if self.traverse_roots(p) == self.traverse_roots(q):
            return "Connected"
        return "Not Connected"
        
    
    def union(self, p, q):
        # Use of root (Trees)
        i = self.traverse_roots(p)
        j = self.traverse_roots(q)

        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.components[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.components[j] = i
            self.sz[i] += self.sz[j]
        

uf = UnionFind(10)
uf.union(4, 3)
uf.union(3, 8)
uf.union(6, 5)
uf.union(9, 4)
uf.union(2, 1)
uf.union(5, 0)
uf.union(7,2)
uf.union(6, 1)
uf.union(7, 3)

begin = time.time()

uf.find(7, 9)
end = time.time()

print(f"Find operation takes {end - begin} secs")