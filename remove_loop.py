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

    def detectandremoveloop(self):
        slow_p = fast_p = self.head

        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                print("loop is there")
                self.removeloop(fast_p.next)
                print("loop is deleted")
                return
        print ("no")

    def removeloop(self,node):
        node.next=None
        
        
##
##    def remove_loop(self):
##        cur_node = self.head
##        li = []
##
##        while cur_node:
##            if cur_node in li:
##                print ("yes")
##                prev_node.next = None
##                print ("loop is deleted")
##                return
##                
##            li.append(cur_node)
##            prev_node = cur_node
##            cur_node = cur_node.next
##        print ("no loop")

l = linked_list()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.push(5)

l.head.next.next.next.next.next = l.head.next.next
l.detectandremoveloop()
l.detectandremoveloop()
