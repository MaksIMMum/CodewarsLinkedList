# class Node():
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next

def stringify(node):
    if node is None:
        return "None"
    res=''
    while node:
        res += f"{node.data} -> "
        node = node.next
    res += "None"
    return res


#print(stringify(Node(0, Node(1, Node(2, Node(3))))))
