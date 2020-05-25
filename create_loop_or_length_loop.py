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

# Function to create a loop in the  
# Linked List. This function creates  
# a loop by connnecting the last node  
# to n^th node of the linked list,  
# (counting first node as 1) 

    def create_loop(self,n):
        loop_node = self.head

        for _ in range(1,n):
            loop_node = loop_node.next

        end_node = self.head

        while end_node.next:
            end_node = end_node.next

        end_node.next = loop_node        

    def length(self):
        cur_node = self.head
        l = []

        while cur_node:
            if cur_node in l:
                print (len(l)-l.index(cur_node))
                return
            l.append(cur_node)
            cur_node = cur_node.next
        print ("loop not exists")

li = linked_list()
li.push(1)
li.push(2)
li.push(3)
li.push(4)
li.create_loop(4)

## Create a loop for testing 
##li.head.next.next.next.next = li.head
li.length()
