class Node: #Represent indivisual element in an link list
    def __init__(self,data=None,next=None,prev=None) -> None:
        self.data=data  # The data 
        self.next=next  # The address of next node (pointer to next element)
        self.prev=prev  # The address of previous node (pointer to previous element)

class Doubled_linked_list:
    def __init__(self):
        self.head=None  #Head  of link list

#In this function set a pointer to head and increnment till end and print all the data 
    def print(self):
        if self.head is None:
            print("Link list is empty")
            return
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+'-->'+'<--'
            itr=itr.next
        print(llstr)

#To append elenment in double link list        
    def append(self,data):
        if self.head is None: # check if there is elenment present in Double linklist
            new_node=Node(data) #create a new node if double link list is empty 
            new_node.prev=None  # set prev of new node ie head to null
            self.head=new_node  # update the status of head pointer , here the new node becomes the head

        #condition when the is elenment present in list so we need to append after the elenment ,ie end of list
        else : 
            new_node=Node(data) #create a new node if double link list is empty
            cur=self.head       #temp variable that goeas from head to end of list
            while cur.next:     #Check if the next to node is Null , if yes then we are at the end of list
                cur=cur.next    #increnment temp variable
            cur.next=new_node
            new_node.prev=cur   #update the new node prev to cur as it contain the last elenment address in it
            new_node.next=None  #set next of new node to Null

#TO add new node before head of link list
    def prepend(self,data):
        if self.head is None: # check if there is elenment present in Double linklist
            new_node=Node(data) #create a new node if double link list is empty 
            new_node.prev=None  # set prev of new node ie head to null
            self.head=new_node  # update the status of head pointer , here the new node becomes the head
        else:
            new_node=Node(data) #create a new node if double link list is empty
            self.head.prev=new_node #set heads prev from Null to new node
            new_node.next=self.head #set next of new node to head
            new_node.prev=None  #set prev of new node ie head to null
            self.head=new_node  ## update the status of head pointer , here the new node becomes the head

if __name__=='__main__':
    a=Doubled_linked_list()
    a.append(12)
    a.append(13)
    a.append(14)
    a.append(16)
    a.append(17)
    a.print()
    a.prepend(11)
    a.prepend(10)
    a.print()