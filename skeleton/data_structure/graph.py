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

class Edge:
    def __init__(self, from_vertex, to_vertex, is_directed = True, **data):
        assert isinstance(from_vertex, Vertex)    
        self.from_vertex = from_vertex

        assert isinstance(to_vertex, Vertex)
        self.to_vertex = to_vertex

        self.is_directed = is_directed
        self.data = data 
    
    def __eq__(self, other):
        if isinstance(self, Edge) and isinstance(other, Edge):
            return self.from_vertex == other.from_vertex and self.to_vertex == other.to_vertex


class AdjList:
    def __init__(self, V, E):
        self.adjacency_list = {v:[] for v in V}
        for edge in E:
            self.adjacency_list[edge.from_vertex].append(edge.to_vertex)
            if not edge.is_directed:
                self.adjacency_list[edge.to_vertex].append(edge.from_vertex)
    def __str__(self):
        result = []
        for vertex, edges in self.adjacency_list.items():
            result.append(f"{vertex}: {', '.join(str(edge)for edge in edges)}")
        return "\n".join(result)

class AdjMatrix:
    def __init__(self, V, E):
        len_V = len(V)
        self.vertex_index = {}
        self.matrix = []
        for i, v in enumerate(V):
            self.vertex_index[v] = i
        for l in range(len_V):
            row = [0]*len_V
            self.matrix.append(row)
        for edge in E:
            i = self.vertex_index[edge.from_vertex]
            j = self.vertex_index[edge.to_vertex]
            self.matrix[i][j] = 1
            if not edge.is_directed:
                self.matrix[j][i] = 1
    def __str__(self):
        result=[]
        for vertex in self.matrix:
            result.append(" ".join(map(str, vertex)))
        return "\n".join(result)
