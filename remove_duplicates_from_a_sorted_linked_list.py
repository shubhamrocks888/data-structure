##Remove duplicates from a sorted linked list
##Write a function which takes a list sorted in non-decreasing order and deletes any duplicate nodes from the list. The list should only be traversed once.
##For example if the linked list is 11->11->11->21->43->43->60 then removeDuplicates() should convert the list to 11->21->43->60.

class node:
    def __init__(self,data=None):
        self.data = data
        self.next =None

class linked_list:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def deletenode(self,prev_node,cur_node):
        prev_node.next = cur_node.next
        

    def removeduplicates(self):
        cur_node = self.head
        prev_node = cur_node
        l = []

        while cur_node:
            if cur_node.data in l:
                self.deletenode(prev_node,cur_node)
                prev_node = prev_node
                cur_node = cur_node.next
            else:
                l.append(cur_node.data)
                prev_node = cur_node
                cur_node = cur_node.next

    def remove_duplicate(self):
        cur_node = self.head

        while cur_node.next:
            if cur_node.data == cur_node.next.data:
                
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next

    def printlist(self):
        cur_node = self.head

        while cur_node:
            print (cur_node.data)
            cur_node = cur_node.next


llist = linked_list()  
  
llist.push(60)  
llist.push(43)  
llist.push(43) 
llist.push(21) 
llist.push(11) 
llist.push(11)
llist.push(11)
print ("Created Linked List: ") 
llist.printlist()  

print("Linked List after removing","duplicate elements:") 
##llist.removeduplicates() 
llist.remove_duplicate()
llist.printlist()  
