from __future__ import print_function

#动态规划
def dp(n):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i < j:
                dp[i][j] = dp[i][i]
            elif i == j:
                dp[i][j] = 1 + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - j][j]
    return dp[n][n]
print("dp: ",dp(5))

'''变种'''

#增加限制条件，每一种划分方案的组成元素不重复
def dp_set(n):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n + 1):
        for j in range(1, n + 1):
            if j > i:
                dp[i][j] = dp[i][i]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - j][j - 1]
    return dp[n][n]

print("dp_set: ",dp_set(5))

#增加限制条件，每一种划分方案规定元素个数
#递归
def rp_limitItem(n,m):
    if n==1 or m == 1:
        return 1
    elif n<m:
        return rp_limitItem(n,n)
    elif n == m:
        return 1+rp_limitItem(n,m-1)
    else:
        return rp_limitItem(n-m,m)+rp_limitItem(n,m-1)
print("rp_limit:",rp_limitItem(5,3))

#动态规划
def dp_limitItem(n,m):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i < j:
                dp[i][j] = dp[i][i]
            elif i == j:
                dp[i][j] = 1 + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - j][j]
    return dp[n][m]
print("dp_limit:",dp_limitItem(5,3))



'''另一种动态规划方法'''
def p(m):
	memo = [[0 for _ in range(m)] for _ in range(m+1)]
	for i in range(m+1):
		memo[i][0] = 1

	for n in range(m+1):
		for k in range(1, m):
			memo[n][k] += memo[n][k-1]
			if n-k > 0:
				memo[n][k] += memo[n-k-1][k]

	return memo[m][m-1]
print(p(100))
