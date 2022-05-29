#Create Node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#Create LL
class LL:
    def __init__(self):
        self.head=None
    
    def insert_at_start(self,data):
        #1 Create temp node
        #2 Point temp node what head was poiniting to earlier
        #3 Point head to temp Node
        new_node=Node(data) 
        new_node.next=self.head
        self.head=new_node
    
    def traverse(self):
        #0 check is List is empty
        #1 Assign head to temp
        #2 temp->temp.ref until temp==null
        if not(self.head):
            return "LL is empty"
        else:
            temp=self.head
            res=[]
            while(temp!=None):
                res.append(temp.data)
                temp=temp.next
            return res

    def length(self):
        if not(self.head):
            return 0
        temp=self.head
        res=0
        while(temp!=None):
            res+=1
            temp=temp.next
        return res
        
    def delete_pos(self,pos):
        if not(self.head):
            return "LL is empty"
        if pos<0:
            return ("Invalid Position: {} | Length: {}".format(pos,l))
        l=self.length()
        if pos>l:
            return ("Invalid Position: {} | Length: {}".format(pos,l))
        temp=self.head
        for i in range(pos-2):
            temp=temp.next
        Del=temp.next
        temp.next=Del.next
        return ("Deleted: {} @ {}".format(Del.data,pos))

    def delete_val(self,val):
        if not(self.head):
            return "LL is empty"
        if self.head.data==val:
            Del=self.head
            self.head=Del.next
            return ("Deleted: {} @ {}".format(Del.data,1))
        temp=self.head
        f=False
        pos=1
        while temp.next:
            if temp.next.data==val:
                f=True
                break
            temp=temp.next
            pos+=1
        if f:
            Del=temp.next
            temp.next=Del.next
            return ("Deleted: {} @ {}".format(Del.data,pos+1))
        return "Not Found"


def main():
    #Crete Object of LL
    newLL=LL()
    newLL.insert_at_start(5)
    newLL.insert_at_start(4)
    newLL.insert_at_start(3)
    newLL.insert_at_start(2)
    newLL.insert_at_start(1)
    print(newLL.traverse())
    print(newLL.length())
    print(newLL.delete_pos(2))
    print(newLL.traverse())
    print(newLL.delete_val(2))
    print(newLL.delete_val(1))
    print(newLL.traverse())

main()