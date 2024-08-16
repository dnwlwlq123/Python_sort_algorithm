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


class DoublyLinkedNode(Node):
    def __init__(self, node_id, datum, prev=None, next=None):
        self.node_id = node_id
        self.datum = datum
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, elements):
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
        return ' <-> '.join(res)


def test_linked_list():
    print("테스트 시작")

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