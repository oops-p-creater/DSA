class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        A=[]
        B=[]
        for i in costs:
            A.append(i[0])
            B.append(i[1])
        minCost=0
        while(len(A)!=0):
            i=0
            if(A[i]==B[i]):
                if A[i+1]<B[i+1]:
                    A[i]=A[i]+1
                else:
                    B[i]=B[i]+1
            if min(A[i],B[i])==A[i]:
                minCost=minCost+A[i]
                temp=min(B[i+1:])
                index=B.index(temp)
            else:
                minCost=minCost+B[i]
                temp=min(A[i+1:])
                index=A.index(temp)
            minCost=minCost+temp
            del A[index]
            del B[index]
            del A[i]
            del B[i]
        return minCost
            
s=Solution()
print(s.twoCitySchedCost([[518,518],[71,971],[121,862],[967,607],[138,754],[513,337],[499,873],[337,387],[647,917],[76,417]]))