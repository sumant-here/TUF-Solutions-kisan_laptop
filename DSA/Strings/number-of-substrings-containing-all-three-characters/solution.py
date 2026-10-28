class Solution:    
    def numberOfSubstrings(self, s: str) -> int:
        #your code goes here
        l = 0 
        count = {'a':0,'b':0,'c':0}
        ans = 0 
        for  r in range(len(s)):
            count[s[r]] += 1
            while count['a'] >  0 and count['b'] > 0 and count['c'] > 0 :
                ans += len(s) - r
                count[s[l]] -= 1
                l     += 1
        return ans
        