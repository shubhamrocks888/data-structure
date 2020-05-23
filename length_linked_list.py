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

    def getcount(self,node):
        
        if not node:
            return 0
        else:
            return 1 + self.getcount(node.next)

    def lengthh(self):
        return self.getcount(self.head)
        

l = linked_list()
l.push(1)
l.push(2)
l.push(3)
l.push(0)
print(l.lengthh())

        
