class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    if head is None:
        return Node(data)
    node = head
    prev = None
    while node:
        if node.data > data:
            if not prev:
                head = Node(data)
                head.next = node
            else:
                prev.next = Node(data)
                prev.next.next = node
            break
        prev = node
        node = node.next
    else:
        prev.next = Node(data)
    return head
