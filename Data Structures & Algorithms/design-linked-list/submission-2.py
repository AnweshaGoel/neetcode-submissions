class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        ptr = self.head.next
        for _ in range(index):
            ptr = ptr.next
        return ptr.val

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head.next
        self.head.next = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return None
        cur = self.head
        for _ in range(index):
            cur = cur.next
        new = Node(val)
        new.next = cur.next
        cur.next = new
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return None
        ptr = self.head
        for _ in range(index):
            ptr = ptr.next
        ptr.next = ptr.next.next
        self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)