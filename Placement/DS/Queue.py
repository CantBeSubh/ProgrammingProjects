#FIFO
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def isEmpty(self):
        return self.front==None

    def enqueue(self,data):
        temp=Node(data)
        if self.rear==None:
            self.front=self.rear=temp
        else:
            self.rear.next=temp
            self.rear=temp

    def display(self):
        temp=self.front
        res=[]
        while temp is not None:
            res.append(temp.data)
            temp=temp.next
        return res
        
    def dequeue(self,data):
        pass

def main():
    q=Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.display())

main()