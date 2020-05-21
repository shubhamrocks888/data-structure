class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def length(self):
        cur_node = self.head
        count = 0

        while cur_node:
            count+=1
            cur_node = cur_node.next

        print (count)


l = linked_list()
l.push(3)
l.push(2)
l.push(1)
l.push(0)
l.length()

        
