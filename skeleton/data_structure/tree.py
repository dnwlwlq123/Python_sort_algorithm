try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node

class TreeNode:
    def __init__(self, node_id, datum=None):
        self.node_id = node_id
        self.datum = datum
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"Tree({self.node_id}, {self.datum})"


class Tree:
    def __init__(self, root_id, children=None):
        self.root = TreeNode(root_id)

        if children is not None:
            self.children = children
        else:
            self.children = []

        for child in self.children:
            if isinstance(child, Tree):
                self.root.add_child(child.root)
            elif isinstance(child, TreeNode):
                self.root.add_child(child)
        print(f"{root_id}")

    # def append(self, datum):
    #     new_node = TreeNode(self.node_id, datum)
    #     if self.children is None:
    #         self.root = new_node
    #         self.children = new_node
    #     else:
    #         self.children.next = new_node
    #         self.children = new_node
    #     self.height += 1
    #
    # def iter_nodes(self):
    #     current = self.children
    #     while current:
    #         yield current.datum
    #         current = current.next
    #
    #
    # def iter_nodes_with_address(self):#inter_nodes_with_address - []1 [0]11
    #     pass
    #
    # def __iter__(self):
    #     cur = self.root
    #     while cur:
    #         yield cur.datum
    #         cur = cur.datum
    #
    # def insert(self, address, elem):#
    #     pass
    #
    # def delete(self, address):
    #     pass
    #
    # def search(self, elem):
    #     pass
    #
    # def root_datum(self):
    #     pass
    #
    # def height(self):
    #     all_height = 0
    #     root_height = 0
    #     child_height = 0
    #     def height_init(all, rh, ch):
    #         all = rh + ch


    def __str__(self):
        child = []
        cur = self.root
        while cur:
            child.append(str(cur.datum))
            cur = cur.datum
        return ' -> '.join(child)


if __name__ == '__main__':
    t1 = Tree(1, [
                Tree(11, [Tree(111), Tree(112)],), 
                Tree(12, [Tree(121), Tree(122), Tree(123),])
             ]
         )
    print(t1)
    
    assert t1.root_datum() == 1 
    assert t1.height() == 3

    for addr, n in t1.iter_nodes_with_address():
        assert [int(e)-1 for e in list(str(n.datum))[1:]] == addr 
        assert t1.search(n.datum) == addr

    t1.insert([2], Tree(13, [Tree(131), Tree(132), Tree(133)]))
    t1.insert([1, 1], Tree(122, [Tree(1221), Tree(1222)]))

    print(t1)
    
    assert 122 == t1.delete([1,2])
    assert 123 == t1.delete([1,2])

    for addr, n in t1.iter_nodes_with_address():
        assert [int(e)-1 for e in list(str(n.datum))[1:]] == addr 
        assert t1.search(n.datum) == addr 

    print(t1)