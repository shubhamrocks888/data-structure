class node:
    def __init__(self,data=None):
        self.data = data
        self.next =None

class linked_list:
    def __init__(self):
        self.head = node()

##TO APPEND A NODE

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

# TO FIND THE LENGTH OF LINKED LIST

    def length(self):
        cur = self.head
        total = 0
        while cur.next:
            total+=1
            cur = cur.next
        return total

# DISPLAY ALL THE ELEMENTS OF A LIST

    def display(self):
        elem=[]
        cur = self.head
        while cur.next:
            cur = cur.next
            elem.append(cur.data)
        return elem
    
# TO GET THE ELEMENTS AT A CERTAIN INDEX

    def get(self,index):
        if index >= my_list.length():
            return "index out of range"
        
##        cur = self.head
##        cur_idx = -1
##        while cur.next:
##            cur_idx+=1
##            cur=cur.next
##            if cur_idx==index:
##                return cur.data
        cur_idx = 0
        cur_node = self.head

        while True:
            cur_node = cur_node.next
            if index==cur_idx:
                return cur_node.data
            cur_idx+=1

##TO ERASE A NODE FROM CERTAIN INDEX

    def erase(self,index):
        if index >= my_list.length():
            return "index out of range"

        cur_idx = 0
        cur_node = self.head

        while True:
            last_node = cur_node
            cur_node = cur_node.next

            if index==cur_idx:
                last_node.next = cur_node.next
                return "node has been deleted"
            cur_idx+=1            

##ADD A NODE AT CERTAIN INDEX

    def add(self,index,data):
        if index >= my_list.length():
            return "index out of range"

        new_node = node(data)
        cur_idx = 0
        cur_node = self.head

        while True:
            last_node = cur_node
            cur_node = cur_node.next

            if index==cur_idx:
                last_node.next = new_node
                new_node.next = cur_node
                return "node has been added"
            cur_idx+=1
            
        
my_list = linked_list()
print (my_list.display())

my_list.append(1)
my_list.append(2)
my_list.append(3)

print (my_list.display())
my_list.add(2,5)
print (my_list.display())
##print (my_list.erase(2))
##print (my_list.display())


