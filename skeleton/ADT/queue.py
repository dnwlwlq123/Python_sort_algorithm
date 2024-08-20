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
<<<<<<< HEAD
=======

        elif self.backend == DoublyLinkedList:
            self.linked_list = DoublyLinkedList(elements)
>>>>>>> 42c02f46707c97c5bf63fa798721b7a722c9c53e

    def elements(self):
        if self.backend == list:
            return self.list
        elif self.backend == LinkedList:
            return list(self.linked_list)

        elif self.backend == LinkedList:
            res = []
            cur = self.linked_list.head

            while cur is not None:
                res.append(cur.datum)
                cur = cur.next

            return res
        
        elif self.backend == DoublyLinkedList:
            res = []
            cur = self.doubly_linked_list.head

            while cur is not None:
                res.append(cur.datum)
                cur = cur.next

            return res

    def enqueue(self, elem):
        if self.backend == list:
            self.list.insert(0, elem)
        elif self.backend == LinkedList:
            self.linked_list.prepend(elem)

        elif self.backend == LinkedList:
            self.linked_list.add_to_head(elem)

        elif self.backend == DoublyLinkedList:
            self.doubly_linked_list.add_to_head(elem)

    def dequeue(self):
        if self.backend == list:
            if not self.list:
                return None
            return self.list.pop()
<<<<<<< HEAD
        elif self.backend == LinkedList:
            if self.linked_list.size == 0:
                return None
            return self.linked_list.pop()

=======
                
        elif self.backend == LinkedList:
            return self.linked_list.delete_from_back()

        elif self.backend == DoublyLinkedList:
            return self.doubly_linked_list.delete_from_back()
    
>>>>>>> 42c02f46707c97c5bf63fa798721b7a722c9c53e
    def front(self):
        if self.backend == list:
            return self.list[-1] if self.list else None
        elif self.backend == LinkedList:
            return self.linked_list.tail.datum if self.linked_list.tail else None

        elif self.backend == LinkedList:
            return self.linked_list.end.datum
        
        elif self.backend == DoublyLinkedList:
            return self.doubly_linked_list.end.datum

    def size(self):
        if self.backend == list:
            return len(self.list)
<<<<<<< HEAD
        elif self.backend == LinkedList:
            return self.linked_list.size

    def is_empty(self):
        if self.backend == list:
            return len(self.list) == 0
        elif self.backend == LinkedList:
            return self.linked_list.is_empty()
=======
    
        elif self.backend == LinkedList:
            return len(self.linked_list)
        
        elif self.backend == LinkedList:
            return self.doubly_linked_list.size

    def is_empty(self):
        return self.size() == 0
        # if self.backend == list:
        #     return self.list == []

        # elif self.backend == LinkedList:
        #     return self.linked_list.size == 0
        
        # elif self.backend == DoublyLinkedList:
        #     return self.doubly_linked_list.size == 0
>>>>>>> 42c02f46707c97c5bf63fa798721b7a722c9c53e

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
<<<<<<< HEAD
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
=======
            return self.elements == other.elements 
        return True 


class PriorityQueue:
    def __init__(self, *elements_with_priority, backend = list):
        """Get list of 2-tuple containing (obj, number), which denotes object and its priority. Higher the number, the element have hight priority. 
        """
        assert isinstance(elements_with_priority, list) or isinstance(elements_with_priority, tuple)

        self.backend = backend

        if self.backend == list:
            self.list = sorted(elements_with_priority, key=lambda x: x[1])
        
        elif self.backend == LinkedList:
            self.linked_list = LinkedList([])
            for element in sorted(elements_with_priority, key=lambda x: x[1], reverse=True):
                self.linked_list.add_to_head(element)
        
        elif self.backend == DoublyLinkedList:
            self.doubly_linked_list = DoublyLinkedList([])
            for element in sorted(elements_with_priority, key=lambda x: x[1], reverse=True):
                self.doubly_linked_list.add_to_head(element)

    
    def elements(self):
        if self.backend == list:
            return self.list
        
        elif self.backend == LinkedList:
            res = []
            cur = self.linked_list.head
            while cur is not None:
                res.append(cur.datum)
                cur = cur.next
            return res
        
        elif self.backend == DoublyLinkedList:
            res = []
            cur = self.doubly_linked_list.head
            while cur is not None:
                res.append(cur.datum)
                cur = cur.next
            return res
        
    def enqueue(self, elem):
        if self.backend == list:
            for idx, e in enumerate(self.list):
                if elem[1] <= e[1]:
                    self.list.insert(idx, elem)
                    break 
            else:
                self.list.append(elem)
            
        elif self.backend == LinkedList:
            new_node = LinkedNode(node_id=0, datum=elem)
            
            if not self.linked_list.head or elem[1] < self.linked_list.head.datum[1]:
                new_node.next = self.linked_list.head
                self.linked_list.head = new_node
            elif elem[1] > self.linked_list.end.datum[1]: # add to end
                self.linked_list.end.next = new_node 
                new_node.next = None 
                self.linked_list.end = new_node
            else:
                current = self.linked_list.head
                while current.next and current.next.datum[1] < elem[1]:
                    current = current.next
                new_node.next = current.next
                current.next = new_node
            
            self.linked_list.size += 1
        
        elif self.backend == DoublyLinkedList:
            new_node = DoublyLinkedNode(node_id=0, datum=elem)

            if not self.doubly_linked_list.head or elem[1] < self.doubly_linked_list.head.datum[1]:
                new_node.next = self.doubly_linked_list.head
                if self.doubly_linked_list.head:
                    self.doubly_linked_list.head.prev = new_node
                self.doubly_linked_list.head = new_node
                self.doubly_linked_list.size += 1

            else:
                current = self.doubly_linked_list.head
                while current.next and current.next.datum[1] <= elem[1]:
                    current = current.next
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                new_node.prev = current
                self.doubly_linked_list.size += 1

    def dequeue(self):
        if self.backend == list:
            return self.list.pop(-1)

        elif self.backend == LinkedList:
            highest_priority = self.linked_list.end.datum
            self.linked_list.delete_from_back()
            return highest_priority

        elif self.backend == DoublyLinkedList:
            highest_priority = self.doubly_linked_list.end.datum
            self.doubly_linked_list.delete_from_back()
            return highest_priority
                
    def front(self):
        if self.backend == list:
            return max(self.list, key=lambda x: x[1])
        elif self.backend == LinkedList:
            return self.linked_list.end.datum
        elif self.backend == DoublyLinkedList:
            return self.doubly_linked_list.end.datum
>>>>>>> 42c02f46707c97c5bf63fa798721b7a722c9c53e

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
            return self.linked_list.size

<<<<<<< HEAD
    def is_empty(self):
        if self.backend == list:
            return self.list == []
        elif self.backend == LinkedList:
            return self.linked_list.is_empty()
=======
        elif self.backend == DoublyLinkedList:
            return len(self.doubly_linked_list) 

    def is_empty(self):
        if self.backend == list:
            return self.list == []
        
        elif self.backend == LinkedList:
            return self.linked_list.size == 0 

        elif self.backend == DoublyLinkedList:
            return self.doubly_linked_list.size == 0
>>>>>>> 42c02f46707c97c5bf63fa798721b7a722c9c53e

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
<<<<<<< HEAD
            return self.elements() == other.elements()
        return False

if __name__ == '__main__':
    available_backends = [LinkedList]

    for backend in available_backends:
        print(f"{backend.__name__}")
        q1 = Queue(1, 2, 3, 4, backend=backend)
        print()

        assert q1.elements() == [1, 2, 3, 4]
=======
            return self.elements == other.elements 
        return True 

if __name__ == '__main__':
    available_backends = [LinkedList] #, LinkedList, DoublyLinkedList]

    for backend in available_backends:
        q1 = Queue(1,2,3,4, backend = backend)
        if backend == DoublyLinkedList:
            print(q1)
        assert q1.elements() == [1,2,3,4], backend
>>>>>>> 42c02f46707c97c5bf63fa798721b7a722c9c53e
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
<<<<<<< HEAD

        if backend == LinkedList:
            print(q1.linked_list, '\t', q2.linked_list)

        q2 = PriorityQueue(('c',1), ('d',4), ('e',2), ('b',3), backend = backend)
        print(f'{q2.elements()}')
        assert q2.elements() == [('c',1), ('e',2), ('b',3), ('d',4)]

        assert q2.size() == 4
        print(f'사이즈 {q2.size()}')
        assert q2.front() == ('d', 4)
        print(f'front {q2.front()}')
=======
        
        if backend == LinkedList:
            print(q1.linked_list, q2.linked_list)

        q2 = PriorityQueue(('c',1), ('d',4), ('e',2), ('b',3), backend = backend)
        assert q2.elements() == [('c',1), ('e',2), ('b',3), ('d',4)], backend  
    
        assert q2.size() == 4
        assert q2.front() == ('d', 4), backend
>>>>>>> 42c02f46707c97c5bf63fa798721b7a722c9c53e
        assert not q2.is_empty()
        # print('q2:', q2, backend)
        # print('q2size is', q2.size(), backend)
        q2.dequeue()
<<<<<<< HEAD
        print(f'{q2.elements()}')
        assert q2.elements() == [('c',1), ('e',2), ('b',3)]
        assert q2.size() == 3
        assert q2.front() == ('b', 3)
=======
        
        assert q2.elements() == [('c',1), ('e',2), ('b',3)], backend
        # print('q2:', q2, backend)
        # print('q2size is', q2.size(), backend)
        assert q2.size() == 3, backend
        assert q2.front() == ('b', 3) 
>>>>>>> 42c02f46707c97c5bf63fa798721b7a722c9c53e
        assert not q2.is_empty()

        q2.enqueue(('x', 0))
        q2.enqueue(('y', 4))
        q2.enqueue(('z', 2))

    
        assert q2.elements() == [('x', 0), ('c',1), ('z', 2), ('e',2), ('b',3), ('y', 4)], backend

        # print('q2:', q2, backend)
        # print('q2size is', q2.size(), backend)
        assert q2.size() == 6, backend
        # print('q2:', q2, backend)
        q2.dequeue()
        # print('five remians:', q2, backend)
        q2.dequeue()
        # print('four remains:', q2, backend)
        q2.dequeue()
        # print('three remains:', q2, backend)
        q2.dequeue()
        # print('two remains:', q2, backend)
        q2.dequeue()
        # print('q2:', q2, backend)  
        q2.dequeue()
        # print('q2:', q2, backend)
        assert q2.is_empty()
        print(f'{q2.elements()}')

