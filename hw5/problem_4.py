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

    def isPalindrome(self):
        # TODO: Please write your code here
        if self._size <= 1:
            return True
        slow = self._head
        fast = self._head
        while fast and fast._next:
            slow = slow._next
            fast = fast._next._next
        prev = None
        curr = slow
        while curr:
            next_node = curr._next
            curr._next = prev
            prev = curr
            curr = next_node
        first_half = self._head
        second_half = prev
        result = True
        while second_half: 
            if first_half._element != second_half._element:
                result = False
                break
            first_half = first_half._next
            second_half = second_half._next
        return result


def main():
    ls1 = SingleLinkedList()
    ls1.insertAtFirst(1)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(1)

    print(ls1)  # Should print: Head-->1-->2-->2-->1-->None
    print(ls1.isPalindrome())  # Should print: True


if __name__ == "__main__":
    main()
