class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def loop_size(node):
    slow = node
    fast = node.next
    last_node = None
    while fast:
        if slow == fast:
            last_node = slow
            break
        slow = slow.next
        fast = fast.next.next
    node = last_node.next
    count = 1
    while node != last_node:
        count += 1
        node = node.next
    return count
