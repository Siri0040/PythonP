class Node(object):
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
class dll(object):
    head = None
    tail = None

    def add(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
    def delete(self, node_value):
        current_node = self.head
        while current_node is not None:
            if current_node.data == node_value:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    self.head = current_node.next
                    current_node.next.prev = None
            current_node = current_node.next
    def show(self):
        print "Data in list:"
        current_node = self.head
        while current_node is not None:
            print current_node.data,
            current_node = current_node.next
d = dll()
d.add(5)
d.add(6)
d.add(5)
d.add(3)
d.show()
d.delete(5)
d.show()
