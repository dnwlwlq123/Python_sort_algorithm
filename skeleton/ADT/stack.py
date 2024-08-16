import sys

sys.path.append('../data_structure')

try:
    from linked_list import LinkedList, LinkedNode
except ModuleNotFoundError:
    from data_structure.linked_list import LinkedList, LinkedNode

class Stack:
    def __init__(self, *elements, backend=LinkedList):
        assert backend in [list, LinkedList]
        self.backend = backend
        if self.backend == list:
            self.list = list(elements)
        elif self.backend == LinkedList:
            self.linked_list = LinkedList(elements)

    def push(self, elem):
        if self.backend == list:
            self.list.append(elem)
        elif self.backend == LinkedList:
            self.linked_list.append(elem)

    def pop(self):
        if self.backend == list:
            return self.list.pop()
        elif self.backend == LinkedList:
            return self.linked_list.pop()

    def top(self):
        if self.backend == list:
            return self.list[-1]
        elif self.backend == LinkedList:
            return self.linked_list.tail.datum if self.linked_list.tail else None

    def is_empty(self):
        if self.backend == list:
            return len(self.list) == 0
        elif self.backend == LinkedList:
            return self.linked_list.is_empty()

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
            return self.linked_list.size

    def elements(self):
        if self.backend == list:
            return self.list
        elif self.backend == LinkedList:
            return self.linked_list.elements()

if __name__ == '__main__':
    available_backends = [LinkedList]

    for backend in available_backends:
        print(f"{backend.__name__}")
        s1 = Stack(3, 2, 1, 4, backend=backend)

        assert s1.top() == 4
        assert not s1.is_empty()
        assert s1.pop() == 4
        assert s1.top() == 1


        s1.push(5)

        assert s1.top() == 5
        assert s1.size() == 4

        assert s1.pop() == 5
        assert s1.pop() == 1
        assert s1.pop() == 2
        assert s1.pop() == 3
        print(f"{s1.elements()}")
        assert s1.is_empty()
