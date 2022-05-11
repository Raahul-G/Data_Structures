class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.insert_at_beginning(data)
            return
        temp = self.head
        while temp.next_node:
            temp = temp.next_node
        temp.next_node = new_node

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_end(self):
        if self.head is None: print("Node is empty")
        temp = self.head
        while temp.next_node.next_node:
            temp = temp.next_node
        temp.next_node = None

    def remove_head(self):
        if self.head is None:
            raise Exception("Node is empty")
        self.head = self.head.next_node

    def listprint(self):
        temp = self.head
        llist = ''
        while temp is not None:
            llist += str(temp.data) + '-->'
            temp = temp.next_node
        print(llist)

    def get_size(self):
        size = 0
        temp = self.head
        while temp:
            size += 1
            temp = temp.next_node
        print("Length of the Linked List", size)

    def remove_at(self, index):
        if index < 0:
            raise Exception("Invalid Index")
        if index == 0:
            self.remove_head()
            return
        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                temp.next_node = temp.next_node.next_node
                break
            temp = temp.next_node
            count += 1

    def insert_at(self, index, data):
        if index < 0: raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        temp = self.head
        while temp:
            temp = temp.next_node
            count += 1
            if count == index - 1:
                node = Node(data, temp.next_node)
                temp.next_node = node
            break


L_list = LinkedList()

L_list.insert_values(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
L_list.listprint()
L_list.get_size()

L_list.remove_end()
L_list.listprint()
L_list.get_size()

L_list.remove_head()
L_list.listprint()
L_list.get_size()

L_list.remove_at(2)
L_list.listprint()
L_list.get_size()

L_list.insert_at(2, "Wednesday")
L_list.listprint()
L_list.get_size()

