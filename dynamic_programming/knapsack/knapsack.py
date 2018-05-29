
"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
"""
def knapsack(W, wt, val, n):
    #建立n行W列数组
    dp = [[0 for i in range(W+1)]for j in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):
            if(wt[i-1]<=w):
                dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    #return dp[n][w]    #返回最大值
    return dp    #返回结果数组

def show(n,W,wt,dp):
    print("最大价值为： ",dp[n][W])
    x = [False for _ in range(n)]
    j = W
    for i in range(1,n+1):
        if dp[i][j]>dp[i-1][j]:
            x[i-1] = True
            j -= wt[i-1]
    print("选择的物品为： ")
    for i in range(n):
        if x[i]:
            print('第',i,'个')
    print(" ")

n=5
W=10
wt=[2,2,6,5,4]
val=[6,3,5,4,6]
dp = knapsack(W,wt,val,n)
print(dp)
show(n,W,wt,dp)
