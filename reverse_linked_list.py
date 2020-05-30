##Reverse a linked list
##Given pointer to the head node of a linked list, the task is to reverse the linked list. We need to reverse the list by changing links between nodes.

##Input: Head of following linked list
##1->2->3->4->NULL
##Output: Linked list should be changed to,
##4->3->2->1->NULL

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

    def reverse(self):
        prev_node = None
        cur_node = self.head

        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

        
    def print_list(self):
        cur_node = self.head

        while cur_node:
            print (cur_node.data,end=" ")
            cur_node = cur_node.next


##BOTH REVERSEUNTIL AND REVERSEE ARE FOR RECURSIVE CALLLING


    def reverseuntil(self,curr,prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        nextt = curr.next
        curr.next = prev
        self.reverseuntil(nextt,curr)

    def reversee(self):
        if self.head is None: 
            return 
        self.reverseuntil(self.head,None)
l = linked_list()
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)
l.print_list()
print("after reversing")
l.reversee()
l.print_list()
        
