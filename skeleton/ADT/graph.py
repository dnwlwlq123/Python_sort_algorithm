import sys



sys.path.append('../data_structure')

try:
    from graph_datastructure import AdjList, AdjMatrix, Vertex, Edge
except ModuleNotFoundError:
    from data_structure.graph_datastructure import AdjList, AdjMatrix, Vertex, Edge


class Graph:
    def __init__(self, V, E, backend = 'adjacent_list'):
        # for v in V:
        #     assert isinstance(v, Vertex)
        # for e in E:
        #     assert isinstance(e, Edge)
        #     assert e.from_vertex in V
        #     assert e.to_vertex in V

        self.V = V 
        self.E = E 
        self.backend = backend

        if backend == 'VE':
            pass 
        elif backend == 'adjacent_list':
            self.backend = 'adjacent_list'
            self.graph = AdjList(V, E)
        elif backend == 'adjacent_matrix':
            self.backend = 'adjacent_matrix'
            self.graph = AdjMatrix(V, E)

    def add_vertex(self, v):
        assert isinstance(v, Vertex)
        if self.backend == 'adjacent_list':
            if v not in self.graph.adjacent_list:
                self.graph.adjacent_list[v] = []
                self.V.append(v)
                print(f"addVertex addVertex {v}")
            else:
                return False
        elif self.backend == 'adjacent_matrix':
            if v in self. graph.vertex_index:
                return False
            else :
                len_V = len(self.graph.vertex_index) + 1
                for row in self.graph.adjacent_matrix:
                    row.append(0)
                self.graph.adjacent_matrix.append([0] * len_V)
                self.graph.vertex_index = len(self.graph.vertex_index)

    
    def remove_vertex(self, v):
        assert isinstance(v, Vertex)
        if self.backend == 'adjacent_list':
            if v in self.graph.adjacent_list:
                for vertex in list(self.graph.adjacent_list.keys()):
                    if v in self.graph.adjacent_list[vertex]:
                        self.graph.adjacent_list[vertex].remove(v)
                del self.graph.adjacent_list[v]
                print(f'삭제된 vertex: {v}')
            else :
                return False
        if self.backend == 'adjacent_matrix':
            if v in self.graph.vertex_index:
                remove_index = self.graph.vertex_index[v]
                self.graph.adjacent_matrix.pop(remove_index)
                for row in self.graph.adjacent_matrix:
                    row.pop(remove_index)
            del self.graph.vertex_index[v]
            for vertex, index in self.graph.vertex_index.items():
                if self.graph.vertex_index > remove_index:
                    self.graph.vertex_index[vertex] - 1
            else:
                return False

    def add_edge(self, e):
        assert isinstance(e, Edge)
        if self.backend == 'adjacent_list':
            if e.from_vertex in self.graph.adjacent_list:
                if e.to_vertex not in self.graph.adjacent_list[e.from_vertex]:
                    self.graph.adjacent_list[e.from_vertex].append(e.to_vertex)
                if not e.is_directed:
                    if e.from_vertex not in self.graph.adjacent_list[e.to_vertex]:
                        self.graph.adjacent_list[e.to_vertex].append(e.from_vertex)
            self.E.append(e)
    def remove_edge(self, e):
        assert isinstance(e, Edge)
        if self.backend == 'adjacent_list':
            if e.from_vertex in self.graph.adjacent_list and e.to_vertex in self.graph.adjacent_list[e.from_vertex]:
                self.graph.adjacent_list[e.from_vertex].remove(e.to_vertex)
                if e.is_directed !=True:
                    self.graph.adjacent_list[e.to_vertex].remove(e.from_vertex)
                self.E.remove(e)
            else :
                return False

    def get_vertices(self):
        if self.backend == 'adjacent_list':
            return list(self.graph.get_vertices())
        elif self.backend == 'adjacent_matrix':
            return list(self.graph.get_vertices())

    def get_edges(self):
        if self.backend == 'adjacent_list':
            return list(self.graph.get_edges())
        elif self.backend == 'adjacent_matrix':
            return list(self.graph.get_edges())

    def get_neighbors(self, v):
        assert isinstance(v, Vertex)
        if self.backend == 'adjacent_list':
            return self.graph.adjacent_list.get(v, [])
        return [] 

    def dfs(self, src):
        assert isinstance(src, Vertex)
        visited = set()
        stack = [src]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(f"dfs방문: {vertex}")
                yield vertex
                for neighbor in (self.graph.adjacent_list.get(vertex, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)




    def bfs(self, src):
        assert isinstance(src, Vertex)
        visited = set()
        queue = [src]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                print(f"bfs방문: {vertex}")
                yield vertex
                for neighbor in self.graph.adjacent_list.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)



    # Do not modify this method

    @staticmethod
    def spring_layout(nodes, edges, iterations=50, k=0.1, repulsion=0.01):
        import numpy as np
        # Initialize positions randomly
        positions = {node: np.random.rand(2) for node in nodes}
        
        for _ in range(iterations):
            forces = {node: np.zeros(2) for node in nodes}
            
            # Repulsive forces between all pairs of nodes
            for i, node1 in enumerate(nodes):
                for j, node2 in enumerate(nodes):
                    if i != j:
                        diff = positions[node1] - positions[node2]
                        dist = np.linalg.norm(diff)
                        if dist > 0:
                            forces[node1] += (diff / dist) * repulsion / dist**2
            
            # Attractive forces for connected nodes
            for edge in edges:
                node1, node2 = edge.from_vertex, edge.to_vertex
                if node1 in positions and node2 in positions:
                    diff = positions[node2] - positions[node1]
                    dist = np.linalg.norm(diff)
                
                if dist > 0:
                    force = k * (dist - 1)  # spring force
                    forces[node1] += force * (diff / dist)
                    forces[node2] -= force * (diff / dist)
            
            # Update positions
            for node in nodes:
                if node in forces:
                    positions[node] += forces[node]
        
        return positions

    def show(self):
        import matplotlib.pyplot as plt
        nodes = self.get_vertices()
        edges = self.get_edges()

        if not nodes or not edges:
                print("없음")
                return

        positions = Graph.spring_layout(nodes, edges)
        if not all(node in positions for node in nodes):
            print("포지션스에 없음")
            return
        plt.figure(figsize=(8, 6))
        ax = plt.gca()

        # Plot nodes
        for node, pos in positions.items():
            ax.scatter(*pos, s=2000, color='lightblue')
            ax.text(*pos, node, fontsize=20, ha='center', va='center')

        # Plot edges
        for edge in edges:
            node1, node2 = edge.from_vertex, edge.to_vertex
            x_values = [positions[node1][0], positions[node2][0]]
            y_values = [positions[node1][1], positions[node2][1]]
            ax.plot(x_values, y_values, color='gray', linewidth=2)

        ax.set_title("Graph Visualization with Spring Layout", fontsize=20)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()
        print(f'backend: {self.backend}')
        print("그래프 구조 :")
        print(self.graph)


if __name__ == '__main__':
    v1 = Vertex(0, 1)
    v2 = Vertex(1, 2)
    v3 = Vertex(2, 3)
    v4 = Vertex(3, 4)
    v5 = Vertex(4, 5)

    e1 = Edge(v1, v2) 
    e2 = Edge(v1, v3) 
    e3 = Edge(v2, v3)
    e4 = Edge(v2, v4)
    e5 = Edge(v3, v5) 
    e6 = Edge(v4, v5)

    V = [v1, v2, v3, v4, v5]
    E = [e1]

    g1 = Graph(V, E, backend='adjacent_list')
    g1.show()

    g1.add_vertex(v2)
    g1.add_vertex(v4)
    g1.add_vertex(v5)
    g1.show()

    # g1.add_edge(e3)
    g1.add_edge(e2)
    g1.add_edge(e3)
    g1.add_edge(e4)
    g1.add_edge(e5)
    g1.add_edge(e6)
    g1.show()

    print("-------------DFS--------------")
    for vertex in g1.dfs(v1):
        ...

    print("-------------BFS--------------")
    for vertex in g1.bfs(v1):
        ...

    # g1.remove_edge(e4)
    g1.remove_vertex(v2)
    g1.show()
    g1.remove_edge(e6)
    g1.show()



