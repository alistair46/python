'''Given a Linked List, the task is to insert a new node in this given Linked List at the following positions: 

1.)At the front of the linked list  
2.)After a given node. '''

class Node: #Represent indivisual element in an link list
    def __init__(self,data=None,next=None) -> None:
        self.data=data  # The data 
        self.next=next  # The address of next node (pointer to next element)

class link_list:
    def __init__(self):
        self.head=None  #Head  of link list

    # Print function to print out i/p & o/p       
    def print(self):
        if self.head is None:
            print("Link list is empty")
            return
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)

# 1.)At the front of the linked list
    def insert_at_begining(self,data):  #To insert data at the begining (i.e before head element)
        node= Node(data,self.head)
        self.head=node

# 2.)After a given node.
    def insert_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.next
        if n is None:
            print("node not present in link_list :",x)
        else:
            node=Node(data)
            node.next=n.next
            n.next=node

if __name__=='__main__':
# manually adding data and creating link list
    a=link_list()
    a.insert_at_begining(1)
    a.insert_at_begining(12)
    a.insert_at_begining(19)
    a.insert_at_begining(25)
    a.print()
    a.insert_after(22,18)
    a.print()