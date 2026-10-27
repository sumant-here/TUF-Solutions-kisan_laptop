class Solution:
    def maxScore(self, cardScore, k):
        #your code goes here
        n = len(cardScore)
        window_len = n - k 
        if window_len == 0 :
            return sum(cardScore)
        win_sum = sum(cardScore[:window_len])
        min_sum = win_sum
        for i in range(window_len,n):
            win_sum += cardScore[i]
            win_sum -= cardScore[i-window_len]
            min_sum = min(min_sum,win_sum)
        return sum(cardScore)-min_sum