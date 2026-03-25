def rearrange_even_odd(self):
    even_head = None
    odd_head = None
    even = None
    odd = None
    curr = self._head

    while curr:
        if curr._element % 2 == 0:
            if even_head is None:
                even_head = curr
                even = even_head
            else:
                even._next = curr
                even = curr
        else:
            if odd_head is None:
                odd_head = curr
                odd = odd_head
            else:
                odd._next = curr
                odd = curr
        curr = curr._next

    if even and odd_head:
        even._next = odd_head
    odd._next = None
    self._head = even_head