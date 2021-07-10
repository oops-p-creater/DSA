class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        n=len(s)
        if n==0 and s==goal:
            return True
        if n==1 and s==goal:
            return True
        for i in range(len(s)):
            s=s[-1]+s[:-1]
            if s == goal:
                return True
        return False
                
                
        