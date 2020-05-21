class node:
    def __init__(self,data=None):
        self.data = data
        self.next =None

class linked_list:
    def __init__(self):
        self.head = None

##TO Add A NODE AT THE  START

    def push(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

##    Time complexity of push() is O(1) as it does constant amount of work.

##ADD A NODE AFTER A GIVEN NODE

    def insertafter(self,prev_node,data):
        if prev_node is None:
            print ("the given previous node must inn linked list")
        new_node = node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        
##Time complexity of insertAfter() is O(1) as it does constant amount of work.

##ADD A NODE AT THE END
        
    def append(self,data):
        new_node = node(data) 
        

        if self.head is None:
            self.head = new_node
            return

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

##Time complexity of append is O(n) where n is the number of nodes in linked list. Since there is a loop from head to end, the function does O(n) work.
##This method can also be optimized to work in O(1) by keeping an extra pointer to tail of linked list/
            
    def printlist(self):
        cur_node = self.head
        while cur_node:
            print (cur_node.data,end=" ")
            cur_node = cur_node.next

l = linked_list()
l.append(6)
l.push(7)
l.push(5)
l.append(8)
l.insertafter(l.head.next,9) 
  
l.printlist()




