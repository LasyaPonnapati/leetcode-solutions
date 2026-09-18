def dailyTemperatures(self, t: list[int]) -> list[int]:
        ans=[0]*len(t)
        s=[]
        for i in range(len(t)-1,-1,-1):
            if not s:
                ans[i]=0
            else:
                if t[s[-1]]>t[i]:
                    ans[i]=s[-1]-i
                else:
                    while t[s[-1]]<t[i] and not s:
                        s.pop()
                    if not s:
                        ans[i]=0
                    else:
                        ans[i]=s[-1]-i
            s.append(i)
        return ans