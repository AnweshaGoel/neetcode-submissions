class ListNode:
    def __init__(self, value):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        point = 0
        while cur:
            if point == index:
                return cur.value
            point += 1
            cur = cur.next
        return -1

    def insertHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head.next
        self.head.next = new
        if not new.next:
            self.tail = new

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while i < index and cur:
            cur = cur.next
            i += 1
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        cur = self.head.next
        res = []
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res
