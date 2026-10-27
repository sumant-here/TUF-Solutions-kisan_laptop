class Solution:
    def totalFruits(self, fruits):
        l = 0 
        basket = {}
        maxi = 0 
        for r in range(len(fruits)):
            basket[fruits[r]] = basket.get(fruits[r],0) + 1
            while len(basket) > 2 :
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0 :
                    del basket[fruits[l]]
                l += 1
            maxi = max(maxi,r-l+1)
        return maxi
