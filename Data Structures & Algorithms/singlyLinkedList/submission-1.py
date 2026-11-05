class Node:
        def __init__(self, val, next = None):
            self.val = val
            self.next = next

class LinkedList:
    
    def __init__(self):
        self.length = 0
        self.head = None
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        node = self.head
        for i in range(index):
            node = node.next
        return node.val

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.length += 1

    def insertTail(self, val: int) -> None:
        if self.length == 0:
            self.insertHead(val)
        else:
            node = self.head
            for i in range(self.length - 1):
                node = node.next
            node.next = Node(val, None)
            self.length += 1

    def remove(self, index: int) -> bool:
        if (index >= self.length):
            return False

        node = self.head
        prevNode = node
        for i in range(index):
            prevNode = node
            node = node.next

        prevNode.next = node.next

        if index == 0:
            self.head = node.next

        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        node = self.head
        arr = [None] * self.length

        for i in range (self.length):
            arr[i] = node.val
            node = node.next
        return arr
        
