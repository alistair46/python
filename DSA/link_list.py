class Node: #Represent indivisual element in an link list
    def __init__(self,data=None,next=None) -> None:
        self.data=data  # The data 
        self.next=next  # The address of next node (pointer to next element)

class link_list:
    def __init__(self):
        self.head=None  #Head  of link list

    def insert_at_begining(self,data):  #To insert data at the begining (i.e before head element)
        node= Node(data,self.head)
        self.head=node

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
            
# A function that will take a list of elements as an input and will create a new fresh LINK_LIST
    def insert_values(self,data_list):
        self.head=None
        for d in data_list:
            self.insert_at_end(d)

#To get length of link_list
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count


if __name__=='__main__':
# manually adding data and creating link list
   ''' a=link_list()
    a.insert_at_begining(1)
    a.insert_at_begining(12)
    a.insert_at_begining(13)
    a.insert_at_begining(14)
    a.print()
    a.insert_at_end(100)
    a.print()'''
   
# to insert values from a list and create a new link list 
   b=link_list()
   b.insert_values(["apple","banana","grapes","mango"])
   b.print()
   print("length of Link_List is:",b.get_length())