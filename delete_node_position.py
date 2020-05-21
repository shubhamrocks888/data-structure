##Input: position = 1, Linked List = 8->2->3->1->7
##Output: Linked List =  8->3->1->7
##
##Input: position = 0, Linked List = 8->2->3->1->7
##Output: Linked List = 2->3->1->7
##



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

    def delete_node(self,position):
        if position==0:
            self.head = self.head.next
            return

        count = 0
        cur_node = self.head

        while count!=position:
            prev_node = cur_node
            cur_node = cur_node.next
            count+=1


        if count == position:
            prev_node.next = cur_node.next
            return
        print ("index out of range")

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print (cur_node.data)
            cur_node = cur_node.next

l = linked_list()
l.push(3)
l.push(2)
l.push(1)
l.push(0)
l.delete_node(3)
l.print_list()
            
            
        
