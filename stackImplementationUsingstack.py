#class for Stack implementation using list
class Stack:
    def __init__(self):
        self.stack=[]   #a constructor which initiliaze a empty list variable for a object
    def push(self,data):
        self.stack.append(data)       # to put data in stack
    def display(self):
        for i in self.stack:          #print stack
            print (i)
    def top(self):
        n=len(self.stack)               #pop and print top element
        item=self.stack[n-1]
        del self.stack[n-1]
        print("poped")
        print(item)
    def isempty(self):
        if(len(self.stack)==0):              #to check empty non empty stack
            return True
        return False

s=Stack()                      # create a element
s.push(5)                           # push further
s.push(6)                               
s.push(7)               
s.display()
s.top()
s.top()

print(s.isempty())
s.display()
    


#output
# 5
# 6
# 7
# poped
# 7
# poped
# 6
# False
# 5





"""
	
# Stack implementation using deque class in Python
 
from collections import deque
 
if __name__ == '__main__':
 
    stack = deque()
 
    print("Inserting 'A' into the stack…")
    stack.append('A')
 
    print("Inserting 'B' into the stack…")
    stack.append('B')
 
    print("Inserting 'C' into the stack…")
    stack.append('C')
 
    print("Inserting 'D' into the stack…")
    stack.append('D')
 
    print("Top element is", stack[-1])                 # prints the stack's top (`D`)
 
    print("Removing", stack.pop(), "from the stack")   # removing the top element (`D`)
    print("Removing", stack.pop(), "from the stack")   # removing the next top (`C`)
 
    # returns the total number of elements present in the stack
    print("The stack size is", len(stack))
 
    print("Removing", stack.pop(), "from the stack")   # removing the top element (`B`)
    print("Removing", stack.pop(), "from the stack")   # removing the next top (`A`)
 
    # check if the stack is empty
    if len(stack) == 0:
        print("The stack is empty")
    else:
        print("The stack is not empty")

        """