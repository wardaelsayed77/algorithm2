
class Graph:
    def __init__(self, vertices):
        self.V = vertices  
        self.edges = [] 
    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))  
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        self.edges.sort()  
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        mst = []  
        e = 0  
        i = 0  

        while e < self.V - 1:
            w, u, v = self.edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

           
            if x != y:
                mst.append((u, v, w))
                e += 1
                self.union(parent, rank, x, y)

       
        print(" The Edges in the MST:")
        for u, v, w in mst:
             print(f"Vertex {u} -- Vertex {v} : Weight {w}")


print("Implementation OF Kruskal's Algorithm ")
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal_mst()
