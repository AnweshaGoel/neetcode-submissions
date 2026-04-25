class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new = Node(value)
        self.tail.prev.next = new
        new.prev = self.tail.prev
        self.tail.prev = new
        new.next = self.tail

    def appendleft(self, value: int) -> None:
        new = Node(value)
        self.head.next.prev = new
        new.next = self.head.next
        self.head.next = new
        new.prev = self.head

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        ans = self.tail.prev
        ans.prev.next = self.tail
        self.tail.prev = ans.prev
        return ans.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        ans = self.head.next
        ans.next.prev = self.head
        self.head.next = ans.next
        return ans.val
