# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        ans=[]
        
        self.solves(A,B,ans)
        
        return ans[::-1]
    def solves(self,A,B,ans):
        if(not A):
            return
        if(A.val==B):
            ans.append(A.val)
            return True
            
        left=self.solves(A.left,B,ans)
        right=self.solves(A.right,B,ans)
        if(left or right):
            ans.append(A.val)
        return left or right
