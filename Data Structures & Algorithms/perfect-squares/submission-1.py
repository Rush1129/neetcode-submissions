class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2,n+1):
            sqrt = int(i**0.5)
            least =  float('inf')
            for j in range(1,sqrt+1):
                sq = j**2
                least = min(least,dp[i-sq])
            dp[i] = 1+least
        return dp[n]