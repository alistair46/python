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


    def getCountRec(self, node):
        if (not node):  # Base case
            return 0
        else:
            return 1 + self.getCountRec(node.next)
 
    # A wrapper over getCountRec()
    def getCount(self):
        return self.getCountRec(self.head)


if __name__=='__main__':
# manually adding data and creating link list
    a=link_list()
    x=1
    a.insert_at_begining(1)
    a.insert_at_begining(12)
    a.insert_at_begining(19)
    a.insert_at_begining(25)
    a.print()
    print("length of link list:",a.getCount())
