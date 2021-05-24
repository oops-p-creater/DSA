class node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
class tree:
    def __init__(self):
        self.root=None
    def insert(self):
        data=int(input())
        temp=node(data)
        if(not self.root):
            self.root=temp
        else:
            queue=[]
            queue.append(self.root)
            while(queue):
                curr=queue[0]
                queue.pop(0)
                if(curr.left):
                    queue.append(curr.left)
                else:
                    curr.left=temp
                    break
                if(curr.right):
                    queue.append(curr.right)
                else:
                     
                    curr.right=temp
                    break
    def display(self):
        q=[]
        if(self.root):
            q.append(self.root)
        else:
            print("empty")
            return
        while(q):
            temp=q[0]
            q.pop(0)
            if(temp.left):
                q.append(temp.left)
            if(temp.right):
                q.append(temp.right)
            print(temp.data,end=" ")
        
                    


        

t1=tree()
t1.insert()
t1.insert()
t1.insert()
t1.insert()
t1.insert()
t1.display()