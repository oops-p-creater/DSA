class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if(len(num1)>len(num2)):
            t=len(num1)-len(num2)
            f='0'*t
            num2=f+num2
        if(len(num1)<len(num2)):
            t=len(num2)-len(num1)
            f='0'*t
            num1=f+num1
        n=max(len(num1),len(num2))-1
        carry=0
        ans=""
        for i in range(n,-1,-1):
            temp=int(num1[i])+int(num2[i])
            temp=temp+carry
            if(temp>=10):
                toAdd=(temp)%10
                toAdd=toAdd
                carry=0
                ans=ans+str(toAdd)
                carry=temp//10
                
            else:
                ans=ans+str(int(temp))
                carry=0
        if(carry!=0):
            ans=ans+str(carry)
        return ans[::-1]
                
            
            
            
            
s=Solution()
print(s.addStrings("456","77"))