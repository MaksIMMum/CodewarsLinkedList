class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if not head or not head.next:
        raise Exception()
    a = head
    b = head.next
    ca = a
    cb = b
    while a and b and b.next:
        a.next = b.next
        b.next = a.next.next
        a = a.next
        b = b.next
    if a:
        a.next = None
    return Context(ca, cb)
