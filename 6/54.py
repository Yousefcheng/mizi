nextv = list(map(int, input().split()))
n = len(nextv)
dp = [0 for _ in range(n + 1)]
for i in range(1, n):
    dp[i] = dp[i - 1] + 1 + dp[i - 1] - dp[nextv[i - 1]] + 1
print(dp[n - 1])