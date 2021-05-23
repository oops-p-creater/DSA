from collections import deque



exp=input("enter expression")
stack=deque()
for i in exp:
    if(i!=')'):
        stack.append(i)
    else:
        if(stack[-1]=='('):
            print("false")
            break
        while(not stack[-1]=='('):
            stack.pop()
        stack.pop()
print("true")
