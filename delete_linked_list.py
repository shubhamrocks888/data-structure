##given a linked list, we need to delete the whole list(free the memory allocation)
##Time Complexity: O(n)
##Auxiliary Space: O(1)

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

    def delete_list(self):
        cur_node = self.head

        while cur_node:
            next_node = cur_node.next
            del cur_node.data
            cur_node = next_node
        print ("linked list deleted")

l = linked_list()
l.push(3)
l.push(2)
l.push(1)
l.push(0)
l.delete_list()

        
