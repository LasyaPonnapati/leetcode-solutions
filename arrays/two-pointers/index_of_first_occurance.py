class Solution:
    def strStr(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        if m>n:
            return -1
        x=0
        while x<n:
            if s[x]==t[0]:
                if s[x:x+m]==t:
                    return x
            x+=1
        return -1
        