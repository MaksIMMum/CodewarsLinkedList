class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None
    nodes = [int(x) for x in list_repr.split(' -> ')[:-1]]
    head = Node(nodes.pop(0), None)
    prev = head
    while nodes:
        new = Node(nodes.pop(0), None)
        prev.next = new
        prev = new
    return head
