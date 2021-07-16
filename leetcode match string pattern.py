class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        d={}
        n=len(pattern)
        s=s.split(" ")
        for i in range (n):
            if( d.get(pattern[i])):
                
                if(d.get(pattern[i])==s[i]):
                    continue
                else:
                    return False
            else:
                if(not s[i] in d.values()):
                    d[(pattern[i])]=s[i]
                else:
                    return False
        return True
s=Solution()
print(s.wordPattern("abba","dog cat cat fish"))