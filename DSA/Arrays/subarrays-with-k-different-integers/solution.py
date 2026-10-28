class Solution:
    def subarraysWithKDistinct(self, nums, k):
        # Your code goes here
        def atmo(k):
            l = 0 
            count = {}
            ans = 0 
            for r in range(len(nums)):
                count[nums[r]] = count.get(nums[r],0) + 1
                while len(count) > k :
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0 :
                        del count[nums[l]]
                    l += 1
                ans += r - l + 1
            return ans 
        return atmo(k) - atmo(k-1)