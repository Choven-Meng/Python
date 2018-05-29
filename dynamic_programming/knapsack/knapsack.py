
"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
"""
'''
01背包问题
'''

def 01_knapsack(W, wt, val, n):
    #建立n行W列数组
    ##初始化dp[N+1][V+1]为0, dp[i][j]表示前i件物品恰放入一个容量为j的背包可以获得的最大价值
    dp = [[0 for i in range(W+1)]for j in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):
            # 总容量w大于等于物品i的容量时，要考虑物品i
            if(wt[i-1]<=w):
                # 注意由于weight、value数组下标从0开始，第i个物品的容量为wt[i-1],价值为val[i-1]
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

'''
完全背包问题
'''
#方法一
def Complete_knapsack1(W, wt, val, n):
    # 初始化f[N+1][V+1]为0，dp[i][j]表示前i件物品恰放入一个容量为j的背包可以获得的最大价值
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):
            #注意wt、val的数组下标从0开始，第i个物品的容量为wt[i-1],价值为val[i-1]
            #W/w[i-1]表示物品i最多可以取几次
            dp[i][w] = dp[i-1][w]
            #初始取k=0为最大，下面的循环是把取了k个物品i能获得的最大价值赋值给dp[i][w]
            for k in range(int(w/wt[i-1])+1):
                if dp[i][w] < dp[i-1][w-k*wt[i-1]]+k*val[i-1]:
                    dp[i][w] = k*val[i-1]+dp[i-1][w-k*wt[i-1]]

        # 上面的f[i][j]也可以通过下面一行代码求得
        #  f[i][w] = max([f[i-1][w-k*wt[i-1]]+k*val[i-1] for k in range(w/wt[i-1]+1)])

    #return dp[n][w]    #返回最大值
    return dp    #返回结果数组

#方法二
def Complete_knapsack2(W, wt, val, n):
    #建立n行W列数组
    dp = [[0 for _ in range(W+1)]for _ in range(n)]

    for i in range(0,n):
        for w in range(1,W+1):
            if(wt[i]<=w):
                dp[i][w] = max(val[i]+dp[i][w-wt[i]],dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    #return dp[n-1][w]    #返回最大值
    return dp    #返回结果数组
'''
多重背包问题
'''
 """
    多重背包问题(每个物品都有次数限制)
    :param n: 物品个数, 如 n=5
    :param W: 背包总容量, 如W=15
    :param wt: 每个物品的容量数组表示, 如wt=[5,4,7,2,6]
    :param val: 每个物品的价值数组表示, 如val=[12,3,10,3,6]
    :param num: 每个物品的个数限制，如num=[2,4,1,5,3]
    :return: 返回最大的总价值
    """

def Multiple_knapsack(W, wt, val, num,n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W + 1):
            #对于物品i最多能取的次数是w/wt[i-1],num[i-1]中较小者
            max_num_i = int(min(w/wt[i-1],num[i-1]))
            dp[i][w] = dp[i-1][w]
            for k in range(max_num_i+1):
                if dp[i][w] < dp[i-1][w-k*wt[i-1]]+k*val[i-1]:
                    dp[i][w] = dp[i-1][w-k*wt[i-1]]+k*val[i-1]
        # 上面的f[i][w]也可以通过下面一行代码求得
        # dp[i][w] = max([f[i-1][w-k*wt[i-1]]+k*val[i-1] for k in range(max_num_i+1)])

    return dp[n][w]    #返回最大值
    #return dp  # 返回结果数组

