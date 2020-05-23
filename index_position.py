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

    def search(self,position):
        cur_node = self.head
        count = 0

        while cur_node:
            if count==position:
                print (cur_node.data)
                return
            count+=1
            cur_node = cur_node.next

        print("invalid position")

##Time Complexity: O(n)

    def getnth(self,position):
        return self.getnthnode(self.head,position)
        

    def getnthnode(self,node,position):
##        if position==0:
##            print (self.head.data)
##            return
        if node:
            count=0
            if count==position:
                print (node.data)
                return
            else:
                return self.getnthnode(node.next,position-1)
        else:
            print ("invalid index position")



            
                

l = linked_list()
l.push(3)
l.push(2)
l.push(1)
l.push(0)
l.getnth(-1)

    
