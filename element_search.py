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

    def search(self,data):
        cur_node = self.head

        while cur_node:
            if cur_node.data==data:
                print ("yes")
                return
            cur_node = cur_node.next

        print ("no")

    def searchh(self,data,node):
        if not node:
            print ("no")
            return

        if node.data==data:
            print ("yes")
            return

        

        return self.searchh(data,node.next)

    

l = linked_list()
l.push(3)
l.push(2)
l.push(1)
l.push(10)
l.searchh(0,l.head)
            
        
