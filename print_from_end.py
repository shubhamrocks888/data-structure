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

    def length(self):
        cur_node = self.head
        count = 0

        while cur_node:
            count+=1
            cur_node = cur_node.next

        return count

    def print_from_end(self,position):
        len = self.length()
        cur_node = self.head

        position = len-position+1

        count =1

        while cur_node:
            if count==position:
                print (cur_node.data)
                return
            count+=1
            cur_node = cur_node.next

        print ("invalid position")

l = linked_list()
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.print_from_end(1)
            
        
