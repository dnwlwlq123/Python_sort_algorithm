import sys
sys.path.append('../data_structure')

try:
    from linked_list import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList
except ModuleNotFoundError:
    from data_structure.linked_list import LinkedList, LinkedNode


class Queue:
    def __init__(self, *elements, backend=LinkedList):
        assert backend in [list, LinkedList]
        self.backend = backend
        if self.backend == list:
            self.list = list(elements)
        elif self.backend == LinkedList:
            self.linked_list = LinkedList(elements)

    def elements(self):
        if self.backend == list:
            return self.list
        elif self.backend == LinkedList:
            return list(self.linked_list)

    def enqueue(self, elem):
        if self.backend == list:
            self.list.insert(0, elem)
        elif self.backend == LinkedList:
            self.linked_list.prepend(elem)

    def dequeue(self):
        if self.backend == list:
            if not self.list:
                return None
            return self.list.pop()
        elif self.backend == LinkedList:
            if self.linked_list.size == 0:
                return None
            return self.linked_list.pop()

    def front(self):
        if self.backend == list:
            return self.list[-1] if self.list else None
        elif self.backend == LinkedList:
            return self.linked_list.tail.datum if self.linked_list.tail else None

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
            return self.linked_list.size

    def is_empty(self):
        if self.backend == list:
            return len(self.list) == 0
        elif self.backend == LinkedList:
            return self.linked_list.is_empty()

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements() == other.elements()
        return False


class PriorityQueue:
    def __init__(self, *elements_with_priority, backend=LinkedList):
        self.backend = backend
        assert backend == LinkedList
        self.linked_list = LinkedList()

        for item, priority in sorted(elements_with_priority, key=lambda x: x[1]):
            self.linked_list.append((item, priority))

    def elements(self):

        elements = []
        current = self.linked_list.head
        while current:
            elements.append(current.datum)
            current = current.next
        return elements

    def enqueue(self, elem):
        if self.backend == list:
            self.list.append(elem)
        elif self.backend == LinkedList:
            return self.linked_list.append(elem)

    def dequeue(self):
        if self.backend == list:
            return self.list.pop()
        elif self.backend == LinkedList:
            return self.linked_list.pop()

    def front(self):
        if self.backend == list:
            return self.list[-1]
        elif self.backend == LinkedList:
            return self.linked_list.tail.datum if self.linked_list.tail else None

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
            return self.linked_list.size

    def is_empty(self):
        if self.backend == list:
            return self.list == []
        elif self.backend == LinkedList:
            return self.linked_list.is_empty()

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements() == other.elements()
        return False

if __name__ == '__main__':
    available_backends = [LinkedList]

    for backend in available_backends:
        print(f"{backend.__name__}")
        q1 = Queue(1, 2, 3, 4, backend=backend)
        print()

        assert q1.elements() == [1, 2, 3, 4]
        assert q1.size() == 4
        print(f'q1.elements : {q1.elements()}')
        print(f'q1.size : {q1.size()}')

        q1.enqueue(5)
        assert q1.elements() == [5, 1, 2, 3, 4]
        print(f'q1.elements {q1.elements()}')

        assert q1.size() == 5
        print(f'q1.size {q1.size()}')

        assert q1.dequeue() == 4
        assert q1.size() == 4
        print(f'q1.size {q1.size()}')

        assert q1.elements() == [5, 1, 2, 3]
        print(f'q1.elements {q1.elements()}')
        assert q1.front() == 3
        print(f'q1.front {q1.front()}')

        print()
        print('----------------------------------------------------')
        print()

        q2 = Queue(backend = backend)

        assert q2.elements() == []
        assert q2.size() == 0
        assert q2.is_empty()

        q2.enqueue(1)

        assert q2.elements() == [1]

        assert q2.size() == 1
        assert not q2.is_empty()

        if backend == LinkedList:
            print(q1.linked_list, '\t', q2.linked_list)

        q2 = PriorityQueue(('c',1), ('d',4), ('e',2), ('b',3), backend = backend)
        print(f'{q2.elements()}')
        assert q2.elements() == [('c',1), ('e',2), ('b',3), ('d',4)]

        assert q2.size() == 4
        print(f'사이즈 {q2.size()}')
        assert q2.front() == ('d', 4)
        print(f'front {q2.front()}')
        assert not q2.is_empty()
        q2.dequeue()
        print(f'{q2.elements()}')
        assert q2.elements() == [('c',1), ('e',2), ('b',3)]
        assert q2.size() == 3
        assert q2.front() == ('b', 3)
        assert not q2.is_empty()

        q2.dequeue()
        q2.dequeue()
        q2.dequeue()
        q2.dequeue()

        assert q2.is_empty()
        print(f'{q2.elements()}')


