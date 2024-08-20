class AdjList:
    def __init__(self, V, E):
        self.adjacent_list = {v:[] for v in V}
        for edge in E:
            self.adjacent_list[edge.from_vertex].append(edge.to_vertex)
            if not edge.is_directed:
                self.adjacent_list[edge.to_vertex].append(edge.from_vertex)
    def __str__(self):
        result = []
        for vertex, edges in self.adjacent_list.items():
            result.append(f"{vertex}: {', '.join(str(edge)for edge in edges)}")
        return "\n".join(result)

    def get_vertices(self):
        return self.adjacent_list.keys()

    def get_edges(self):
        edges = []
        for from_vertex, to_vertices in self.adjacent_list.items():
            for to_vertex in to_vertices:
                edges.append(Edge(from_vertex, to_vertex))
        return edges

class AdjMatrix:
    def __init__(self, V, E):
        len_V = len(V)
        self.vertex_index = {}
        self.adjacent_matrix = []
        for i, v in enumerate(V):
            self.vertex_index[v] = i
        for l in range(len_V):
            row = [0]*len_V
            self.adjacent_matrix.append(row)
        for edge in E:
            i = self.vertex_index[edge.from_vertex]
            j = self.vertex_index[edge.to_vertex]
            self.adjacent_matrix[i][j] = 1
            if not edge.is_directed:
                self.adjacent_matrix[j][i] = 1


    def __str__(self):
        result=[]
        for vertex in self.adjacent_matrix:
            result.append(" ".join(map(str, vertex)))
        return "\n".join(result)


class Vertex:
    def __init__(self, node_id, datum):
        self.datum = datum
        self.node_id = node_id

    def __eq__(self, other):
        if isinstance(self, Vertex) and isinstance(other, Vertex):
            return self.node_id == other.node_id
        return False

    def __hash__(self):
        return hash((self.node_id, self.datum))

    def __str__(self):
        return str(self.datum)

    # def __repr__(self):
    #     return f"순회 결과 : {self.node_id}"


class Edge:
    def __init__(self, from_vertex, to_vertex, is_directed=True, **data):
        assert isinstance(from_vertex, Vertex)
        self.from_vertex = from_vertex

        assert isinstance(to_vertex, Vertex)
        self.to_vertex = to_vertex

        self.is_directed = is_directed
        self.data = data

    def __eq__(self, other):
        if isinstance(self, Edge) and isinstance(other, Edge):
            return self.from_vertex == other.from_vertex and self.to_vertex == other.to_vertex

    def __repr__(self):
        return f"Edge({self.from_vertex} -> {self.to_vertex})"

v1 = Vertex(1, "A")
v2 = Vertex(2, "B")
v3 = Vertex(3, "C")
v4 = Vertex(4, "D")
v5 = Vertex(5, "E")
v6 = Vertex(6, "F")
v7 = Vertex(7, "G")


e1 = Edge(v1, v2)
e2 = Edge(v2, v4, is_directed=False)
e3 = Edge(v2, v5, is_directed=False)
e4 = Edge(v3, v6, is_directed=False)
e5 = Edge(v3, v7, is_directed=False)

V = [v1, v2, v3, v4, v5, v6, v7]
E = [e1, e2, e3, e4, e5]


adj_list = AdjList(V, E)
adj_matrix = AdjMatrix(V, E)

print("List:")
print(adj_list)

print("\nMatrix:")
print(adj_matrix)