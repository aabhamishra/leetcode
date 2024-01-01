class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(s) == 0:
            return 0

        g.sort()
        s.sort()

        cookie, child = 0,0
        res = 0

        while cookie < len(s) and child < len(g):
            if s[cookie] >= g[child]:
                res+=1
                child+=1
            
            cookie+=1
        

        return res