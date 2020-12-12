class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def element(self):
        return self.value


class LinkedList:

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __init__(self, *values):
        self.head = self.tail = self.current = None
        self.length = 0
        if values is not None:
            for value in values:
                self.push(value)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return self.node_at_index(index)

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __setitem__(self, key, node):
        if key == 0:
            self.head = self.tail = node
        else:
            nodeBefore = self[key - 1]
            node.next = nodeBefore.next.next
            nodeBefore.next = node

    def empty(self):
        return not self.empty

    def node_at_index(self, index):
        if index >= self.length or abs(index) > self.length:
            raise IndexError()
        elif index == -1:
            return self.tail
        elif index < 0:
            return self.node_at_index(self.length + index)
        else:
            current = self.head
            for i in range(index):
                if not current.next:
                    raise IndexError()
                current = current.next
            return current

    def push_front(self, node):
        node.next = self.head
        self.head = node
        self.length += 1

    def pop_front(self):
        self.head = self.head.next
        self.length -= 1

    def push(self, node):
        if self.length == 0:
            self.head = self.tail = node
            self.length += 1
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1

    def push_wrapped(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = self.tail = node
            self.length += 1
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1

    def pop(self):
        current = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return current
        else:
            for i in range(self.length - 2):
                current = current.next
            current.next = None
            self.tail = current
        self.length -= 1
        return current

    def erase_at(self, index):
        if self.length == 0:
            raise IndexError()
        else:
            if index == 0:
                self.head = self.head.next
            else:
                node = self.node_at_index(index - 1)
                node.next = node.next.next
            self.length -= 1
