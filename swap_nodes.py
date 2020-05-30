##Swap nodes in a linked list without swapping data
##Given a linked list and two keys in it, swap nodes for two given keys. Nodes should be swapped by changing links. Swapping data of nodes may be expensive in many situations when data contains many fields.
##It may be assumed that all keys in linked list are distinct.
##
##Examples:
##
##Input:  10->15->12->13->20->14,  x = 12, y = 20
##Output: 10->15->20->13->12->14
##
##Input:  10->15->12->13->20->14,  x = 10, y = 20
##Output: 20->15->12->13->10->14
##
##Input:  10->15->12->13->20->14,  x = 12, y = 13
##Output: 10->15->13->12->20->14

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

    def swap(self,first,second):
        cur_node =self.head
        l= []

        while cur_node:
            if len(l)==2:
                break
            if cur_node.data==first or cur_node.data==second:
                l.append(cur_node)
            cur_node = cur_node.next
        l[0].data,l[1].data = l[1].data,l[0].data

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print (cur_node.data,end = " ")
            cur_node =cur_node.next

li = linked_list()
li.push(14)
li.push(20)
li.push(13)
li.push(12)
li.push(15)
li.push(10)
li.print_list()
print ("after swapping")
li.swap(12,13)
li.print_list()
