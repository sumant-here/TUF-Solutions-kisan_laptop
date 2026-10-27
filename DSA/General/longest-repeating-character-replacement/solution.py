class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        count = {}
        maxi = 0 
        ans = 0 
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            maxi = max(maxi,count[s[r]])


            
            while (r-l+1) - maxi > k :
                count[s[l]] -= 1
                l += 1
            ans = max(ans,r-l+1)
        return ans 
        