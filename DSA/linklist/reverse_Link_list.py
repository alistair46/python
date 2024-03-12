class Node: #Represent indivisual element in an link list
    def __init__(self,data=None,next=None) -> None:
        self.data=data  # The data 
        self.next=next  # The address of next node (pointer to next element)

class link_list:
    def __init__(self):
        self.head=None  #Head  of link list

    def insert_at_end(self,data):
        if self.head is None:  #to check if the link list is blank
            self.head=Node(data,None) #insert element will become head
            return
        itr=self.head
        while itr.next:
            itr=itr.next # TO iterate at the end of linklist 
        itr.next=Node(data, None) # to add new data at the end of list

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

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev



if __name__=='__main__':
# manually adding data and creating link list
    a=link_list()
    a.insert_at_end(1)
    a.insert_at_end(3)
    a.insert_at_end(6)
    a.insert_at_end(8)
    a.insert_at_end(15)
    a.insert_at_end(19)
    a.insert_at_end(17)
    a.insert_at_end(25)
    a.print()
    a.reverse()
    a.print()
  
