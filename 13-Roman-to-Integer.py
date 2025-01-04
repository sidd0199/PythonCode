class Solution:
    def romanToInt(self, s: str) -> int:
        dic = { 'I':1 ,'V':5, 'X':10, 'L':50,
        'C':100, 'D':500, 'M':1000}
        temp = 0
        ans =0

        for i in range (0,len(s)-1):
            if dic[s[i]] >= dic[s[i+1]]:
                ans= dic[s[i]]+ans

            if dic[s[i]] < dic[s[i+1]]:
                ans= ans - dic[s[i]]
        ans= ans+dic[s[-1]]
        return ans
