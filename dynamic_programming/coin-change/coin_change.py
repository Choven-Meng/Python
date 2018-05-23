# coding=utf-8
from __future__ import print_function

#计算构成n的组合数
def coin_count(S,  n):
    table = [0] * (n + 1)

    # Base case (If given value is 0)
    table[0] = 1

    # Pick all coins one by one and update table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0, len(S)):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]
    return table[n]

#S中元素组合为n的最优组合个数
def coin_selection(S,n):
    min_coin_num = [0]
    for i in range(1,n+1):
        min_coin_num.append(float('inf'))
        for value in S:
            if value<=i and min_coin_num[i-value]+1<min_coin_num[i]:
                min_coin_num[i]= min_coin_num[i-value]+1
    return min_coin_num[n]

if __name__ == '__main__':
    print(coin_count([1, 2, 3],  4))  # answer 4
    print(coin_selection([1,2,3],7))  #answer 3
    print(coin_count([2, 5, 3, 6],  10))  # answer 5
    print(coin_selection([2,5,3,6],10))   #answer 2
