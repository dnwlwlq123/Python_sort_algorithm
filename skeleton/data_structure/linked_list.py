try:
    from node import Node
except ModuleNotFoundError:
    from data_structure.node import Node


class LinkedNode:
    def __init__(self, node_id, datum, next=None):
        self.node_id = node_id
        self.datum = datum
        self.next = next

class LinkedList:
<<<<<<< HEAD
    def __init__(self, elements=None):
        self.head = None
        self.tail = None
        self.size = 0
        if elements:
            for element in elements:
                self.append(element)

    def prepend(self, datum):
        new_node = LinkedNode(0, datum)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def append(self, datum):
        new_node = LinkedNode(self.size, datum)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop(self):
        if self.head is None:
            return None

        if self.head == self.tail:
            datum = self.head.datum
            self.head = None
            self.tail = None
        else:
            cur = self.head
            while cur.next != self.tail:
                cur = cur.next
            datum = self.tail.datum
            self.tail = cur
            self.tail.next = None

        self.size -= 1
        return datum

    def is_empty(self):
        return self.size == 0

    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    def elements(self):
        elements = []
        cur = self.head
        while cur:
            elements.append(cur.datum)
            cur = cur.next
        return elements

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.datum
            cur = cur.next

    def __str__(self):
        res = []
        cur = self.head
        while cur:
            res.append(str(cur.datum))
            cur = cur.next
        return ' -> '.join(res)
=======
    def __init__(self, elements):
    
        if not elements:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
        else:
            elements = list(elements)

            for idx, elem in enumerate(elements):
                if not isinstance(elem, LinkedNode):
                   elements[idx] = LinkedNode(idx, elem)
                    
            self.head = elements[0]
            self.end = elements[-1]

            for idx, elem in enumerate(elements):
                if idx == len(elements)-1:
                    elem.next = None
                else:  
                    elem.next = elements[idx+1]
                
            self.tail = LinkedList(elements[1:])
            self.size = len(elements)

    def add_to_head(self, elem):
        new_node = LinkedNode(0, elem)
        new_node.next = self.head
        self.head = new_node
        
        if self.end is None:
            self.end = new_node
        self.size += 1

    def delete_from_back(self):
        # print('before', self, self.end.datum)
        if self.size == 0:
            return None

        if self.size == 1:
            deleted_node = self.end
            self.head = None
            self.end = None
            self.size -= 1
            
            return deleted_node.datum

        cur = self.head
        while cur.next != self.end:
            cur = cur.next
        assert cur.next == self.end 
        # from code import interact
        # if self.end.datum == ('y', 4):
        #     interact(local = locals())
        deleted_node = self.end
        self.end = cur
        self.end.next = None
        self.size -= 1
        # print('after', self, self.end.datum)

        return deleted_node.datum

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.datum
            current = current.next
            
    def __str__(self):
        res = []
        current = self.head
        while current is not None:
            res.append(str(current.datum))
            current = current.next
        return ' -> '.join(res)

    def __len__(self):
        return self.size
>>>>>>> 42c02f46707c97c5bf63fa798721b7a722c9c53e


class DoublyLinkedNode(Node):
    def __init__(self, node_id, datum, prev=None, next=None):
        self.node_id = node_id
        self.datum = datum
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, elements):
<<<<<<< HEAD
        self.head = None
        self.tail = None
        self.size = 0

        for index, element in enumerate(elements):
            new_node = DoublyLinkedNode(node_id=index, datum=element)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            self.size += 1
=======
        if elements is None:
            elements = []
        elements = list(elements)
>>>>>>> 42c02f46707c97c5bf63fa798721b7a722c9c53e

        if not elements:
            self.head = None
            self.tail = None
            self.size = 0
       
        else:
            for idx, elem in enumerate(elements):
                if not isinstance(elem, DoublyLinkedNode):
                   elements[idx] = DoublyLinkedNode(idx, elem)
                    
            self.head = elements[0]
            self.end = elements[-1]

            for idx, elem in enumerate(elements):
                if idx == len(elements)-1:
                    elem.next = None
                else:  
                    elem.next = elements[idx+1]

            for idx, elem in enumerate(elements):
                if idx == 0:
                    elem.prev = None
                else:  
                    elem.prev = elements[idx-1]
                
            self.tail = DoublyLinkedList(elements[1:])
            self.size = len(elements)  

    def add_to_head(self, elem):
        new_node = DoublyLinkedNode(0, elem)
        
        if self.head is None:
            self.head = new_node
            self.end = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.size += 1

    def delete_from_back(self):
        if self.size == 0:
            return None

        deleted_node = self.end

        if self.size == 1:
            self.head = None
            self.end = None
        else:
            self.end = self.end.prev
            self.end.next = None

        self.size -= 1
        return deleted_node.datum
        
    def __iter__(self):
<<<<<<< HEAD
        cur = self.head
        while cur:
            yield cur.datum
            cur = cur.next

    def __str__(self):
        res = []
        cur = self.head
        while cur:
            res.append(str(cur.datum))
            cur = cur.next
        return ' <-> '.join(res)

    def elements(self):
        elements = []
        cur = self.head
        while cur:
            elements.append(cur.datum)
            cur = cur.next
        return elements

def test_linked_list():

    # 초기화
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    linked_list = LinkedList(elements)

    # 초기 상태 출력
    print("초기 LinkedList 상태:")
    print(linked_list)
    print('사이즈 :', linked_list.size)

    # Append 테스트
    linked_list.append(11)
    print("11을 append 한 후 LinkedList 상태:")
    print(linked_list)
    print('사이즈 :', linked_list.size)

    # Prepend 테스트
    linked_list.prepend(12)
    print("0을 prepend 한 후 LinkedList 상태:")
    print(linked_list)
    print('사이즈 :', linked_list.size)

    # Pop 테스트
    popped_value = linked_list.pop()
    print(f"pop() 호출로 제거된 값: {popped_value}")
    print("pop() 후 LinkedList 상태:")
    print(linked_list)
    print('사이즈 :', linked_list.size)

    # 추가 pop 테스트
    popped_value = linked_list.pop()
    print(f"pop() 호출로 제거된 값: {popped_value}")
    print("추가 pop() 후 LinkedList 상태:")
    print(linked_list)
    print('사이즈 :', linked_list.size)


# 테스트 함수 호출
test_linked_list()
=======
        current = self.head
        while current is not None:
            yield current.datum
            current = current.next

    def __str__(self):
        res = []
        current = self.head
        while current is not None:
            res.append(str(current.datum))
            current = current.next
        return ' -> '.join(res) 

if __name__ == '__main__':
    lst = LinkedList([1,2,3])

    print(lst) 
    print(LinkedList.__str__(lst))
    str(lst)
    LinkedList.__str__(lst)
    
>>>>>>> 42c02f46707c97c5bf63fa798721b7a722c9c53e
