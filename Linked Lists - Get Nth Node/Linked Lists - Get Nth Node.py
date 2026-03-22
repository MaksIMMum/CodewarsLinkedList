# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    if not node or index < 0:
        raise Exception()
    for _ in range(index):
        node = node.next
        if not node:
            raise Exception()
    return node
