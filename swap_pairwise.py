##Pairwise swap elements of a given linked list
##Given a singly linked list, write a function to swap elements pairwise.
##
##Input : 1->2->3->4->5->6->NULL
##Output : 2->1->4->3->6->5->NULL
##
##Input : 1->2->3->4->5->NULL
##Output : 2->1->4->3->5->NULL

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

    def swap(self):
        cur_node = self.head

        while cur_node and cur_node.next:
        
                cur_node.data,cur_node.next.data = cur_node.next.data,cur_node.data
                cur_node = cur_node.next.next
            

    def print_list(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data,end=" ")
            cur_node = cur_node.next

l = linked_list()
l.push(6)
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.print_list()
print ("after swapping")
l.swap()
l.print_list()
    
