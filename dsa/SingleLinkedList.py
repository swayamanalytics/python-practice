from LinkedList import Node

class SingleLinkedList(object):
    def __init__(self,node=None):
        self.head = node
        node.next=None
        if node is not None:
            self.__length=1
        else:
            self.__length=0

    def length(self):
        curnode=self.head
        count=0
        while curnode is not None:
            count+=1
            curnode=curnode.next
        return count
    
    def insertatBeginning(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
        self.__length+=1

    def insertatEnd(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            currentnode=self.head
            while currentnode.next is not None:
                currentnode=currentnode.next
            currentnode.next=node
        self.__length+=1

    def insertatpoistion(self,data,pos):
        newnode=Node(data)
        if pos < 0 or pos > self.__length+1:
            raise ValueError("Wrong Position")
        else:
            if pos == self.__length+1:
                self.insertatEnd(data)
            elif pos == 0:
                self.insertatBeginning(data)
            else:
                curr=self.head
                count=1
                while count < pos-1:
                    count+=1
                    curr=curr.next

                newnode.next=curr.next
                curr.next=newnode
        self.__length+=1
                


    

    def traverse(self):
        current=self.head
        #print(current.data)
        while current is not None:
            print(current.data)
            current=current.next

    
        

node1=Node(data=52)
list1=SingleLinkedList(node1)
list1.insertatBeginning(53)
list1.insertatEnd(55)
#print(list1.head)
list1.insertatpoistion(66,2)
#print(list1.head.data)
#df=list1.length()
list1.traverse()