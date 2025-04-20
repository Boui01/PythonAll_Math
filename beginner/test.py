class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_item(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def delete_item(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.data == item:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                break
            previous = current
            current = current.next

my_list = LinkedList()
my_list.add_item("apple")
my_list.add_item("banana")
my_list.delete_item("apple")
current = my_list.head
while current:
    print(current.data)
    current = current.next


