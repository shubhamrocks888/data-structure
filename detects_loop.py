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

    def loop(self):
        cur_node = self.head
        s = set()

        while cur_node:
            if cur_node in s:
                print ("yes")
                return
            s.add(cur_node)
            cur_node = cur_node.next
        print ("no")
    

##Approach using Mark Visited Nodes: This solution requires modifications to the basic linked list data structure.
##
##Have a visited flag with each node. 
##Traverse the linked list and keep marking visited nodes. 
##If you see a visited node again then there is a loop. This solution works in O(n) but requires additional information with each node.
##A variation of this solution that doesn’t require modification to basic data structure can be implemented using a hash, just store the addresses of visited nodes in a hash and if you see an address that already exists in hash then there is a loop
##.

##Floyd’s Cycle-Finding Algorithm: This is the fastest method and has been described below:
##
##Traverse linked list using two pointers. 
##Move one pointer(slow_p) by one and another pointer(fast_p) by two. 
##If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list doesn’t have a loop

    def detects_loop(self):
        slow_p = self.head
        fast_p = self.head

        while (slow_p and fast_p and fast_p.next.next ):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p ==fast_p:
                print ("yes")
                return
        print ("no")


li = linked_list()
li.push(1)
li.push(2)
li.push(3)
li.push(4)
## Create a loop for testing 
li.head.next.next.next.next = li.head
li.loop()
