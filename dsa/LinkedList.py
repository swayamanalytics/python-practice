class Node(object):
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    def getItem(self):
        return self.data
    def setItem(self,data):
        self.data=data
    def getNext(self):
        return self.next
    def setNext(self,node):
        self.node=node
    def hasNext(self):
        if self.next is not None:
            return True
        else:
            return False