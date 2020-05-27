##Remove duplicates from an unsorted linked list
##Write a removeDuplicates() function which takes a list and deletes any duplicate nodes from the list. The list is not sorted.
##For example if the linked list is 12->11->12->21->41->43->21 then removeDuplicates() should convert the list to 12->11->21->41->43.

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

    def removeduplicate(self):
        cur_node = self.head
        prev_node = cur_node
        l = []

        while cur_node:
            if cur_node.data in l:
                prev_node.next = cur_node.next
                prev_node = prev_node
                cur_node = cur_node.next
            else:
                l.append(cur_node.data)
                prev_node = cur_node
                cur_node = cur_node.next

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print (cur_node.data)
            cur_node = cur_node.next

li = linked_list()
li.push(12)
li.push(11)
li.push(12)
li.push(21)
li.push(41)
li.push(43)
li.push(21)

li.print_list()
print ("after removing duplicate is")
li.removeduplicate()
li.print_list()
