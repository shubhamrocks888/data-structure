##Created Linked List:
## 2  3  1  7
##Linked List after Deletion of 1:
## 2  3  7




class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self,data):

        if self.head.data==data:
            self.head = self.head.next
            return

        cur_node = self.head
        while cur_node:
            if cur_node.data==data:
                prev_node.next = cur_node.next
                return

            prev_node = cur_node
            cur_node = cur_node.next

    def print_list(self):
        cur_node =self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

l = linked_list()
l.push(1)
l.push(1)
l.push(1)
l.push(1)
l.delete_node(1)
l.print_list()
