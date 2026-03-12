class SingleLinkedList:
    class Node:
        def __init__(self, element=None, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insertAtFirst(self, e):
        newNode = self.Node(e, self._head)
        self._head = newNode
        self._size += 1

    def deleteFirst(self):
        if self.is_empty():
            raise Exception('LinkedList is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def deleteLast(self):
        if self.is_empty():
            raise Exception('LinkedList is empty')
        prv = None
        cur = self._head
        while cur._next is not None:
            cur = cur._next
            prv = prv._next if prv is not None else self._head
        if prv is None:
            self._head = None
        else:
            prv._next = None
        self._size -= 1
        return cur._element

    def unOrderedSearch(self, target):
        currNode = self._head
        while currNode is not None and currNode._element != target:
            currNode = currNode._next
        return currNode is not None

    def __str__(self):
        result = "Head-->"
        currNode = self._head
        while currNode is not None:
            result += str(currNode._element) + "-->"
            currNode = currNode._next
        return result + "None"

    def sortList(self):
        # TODO: Please write your code here  
        if self._size <= 1:
            return
        dummy = self.Node(0)
        dummy._next = self._head
        
        step = 1
        while step < self._size:
            prev_tail = dummy
            curr = dummy._next
            
            while curr:
                left = curr
                for i in range(step - 1):
                    if curr._next:
                        curr = curr._next
                    else:
                        break
                right = curr._next
                curr._next = None 
                curr = right
                for i in range(step - 1):
                    if curr and curr._next:
                        curr = curr._next
                    else:
                        break
                
                next_start = None
                if curr:
                    next_start = curr._next
                    curr._next = None 
                l1, l2 = left, right
                while l1 and l2:
                    if l1._element < l2._element:
                        prev_tail._next = l1
                        l1 = l1._next
                    else:
                        prev_tail._next = l2
                        l2 = l2._next
                    prev_tail = prev_tail._next
                prev_tail._next = l1 if l1 else l2
                while prev_tail._next:
                    prev_tail = prev_tail._next
                curr = next_start
            step *= 2
        self._head = dummy._next


def main():
    ls1 = SingleLinkedList()
    ls1.insertAtFirst(3)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(6)
    ls1.insertAtFirst(5)

    print(ls1)  # Should print: Head-->5-->6-->2-->3-->None
    ls1.sortList()
    print(ls1)  # Should print: Head-->2-->3-->5-->6-->None


if __name__ == "__main__":
    main()
