##Move last element to front of a given Linked List
##Write a function that moves the last element to the front in a given Singly Linked List.
##For example, if the given Linked List is 1->2->3->4->5, then the function should change the list to 5->1->2->3->4.

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

        while cur_node.next:
            cur_node =cur_node.next
        self.head.data,cur_node.data = cur_node.data,self.head.data

    def print_list(self):
        cur_node = self.head

        while cur_node:
            print (cur_node.data,end=" ")
            cur_node = cur_node.next

l = linked_list()
##l.push(5)
##l.push(4)
##l.push(3)
##l.push(2)
l.push(1)
l.print_list()
print("after swapping")
l.swap()
l.print_list()

    
