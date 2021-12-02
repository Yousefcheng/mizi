s = input()
d = int(input())
n = len(s)
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for len in range(2, n + 1):
    for i in range(n - len + 1):
        j = i + len - 1
        if s[i] == s[j]:
            dp[i][j] = dp[i + 1][j - 1] + 2
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        # cnt = max(dp[i][j], cnt)

if dp[0][n - 1] >= n - d:
    print("True")
else:
    print("False")