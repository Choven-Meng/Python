## 问题描述

什么是最长公共子序列呢?好比一个数列 S，如果分别是两个或多个已知数列的子序列，且是所有符合此条件序列中最长的，则S 称为已知序列的最长公共子序列。

举个例子，如：有两条随机序列，如 1 3 4 5 5 ，and 2 4 5 5 7 6，则它们的最长公共子序列便是：4 5 5。

注意最长公共子串（Longest CommonSubstring）和最长公共子序列（LongestCommon Subsequence, LCS）的区别：子串（Substring）是串的一个连续的部分，子序列（Subsequence）则是从不改变序列的顺序，而从序列中去掉任意的元素而获得的新序列

## 解决思路：动态规划算法

 事实上，最长公共子序列问题也有最优子结构性质。

记:

Xi=﹤x1，⋯，xi﹥即X序列的前i个字符 (1≤i≤m)（前缀）

Yj=﹤y1，⋯，yj﹥即Y序列的前j个字符 (1≤j≤n)（前缀）

假定Z=﹤z1，⋯，zk﹥∈LCS(X , Y)。

  > 若xm=yn（最后一个字符相同），则不难用反证法证明：该字符必是X与Y的任一最长公共子序列Z（设长度为k）的最后一个字符，即有zk = xm = yn 且显然有Zk-1∈LCS(Xm-1 , Yn-1)即Z的前缀Zk-1是Xm-1与Yn-1的最长公共子序列。此时，问题化归成求Xm-1与Yn-1的LCS（LCS(X , Y)的长度等于LCS(Xm-1 , Yn-1)的长度加1）。

  > 若xm≠yn，则亦不难用反证法证明：要么Z∈LCS(Xm-1, Y)，要么Z∈LCS(X , Yn-1)。由于zk≠xm与zk≠yn其中至少有一个必成立，若zk≠xm则有Z∈LCS(Xm-1 , Y)，类似的，若zk≠yn 则有Z∈LCS(X , Yn-1)。此时，问题化归成求Xm-1与Y的LCS及X与Yn-1的LCS。LCS(X , Y)的长度为：max{LCS(Xm-1 , Y)的长度, LCS(X , Yn-1)的长度}。

  > 由于上述当xm≠yn的情况中，求LCS(Xm-1 , Y)的长度与LCS(X , Yn-1)的长度，这两个问题不是相互独立的：两者都需要求LCS(Xm-1，Yn-1)的长度。另外两个序列的LCS中包含了两个序列的前缀的LCS，故问题具有最优子结构性质考虑用动态规划法。

  > 也就是说，解决这个LCS问题，你要求三个方面的东西：1、LCS（Xm-1，Yn-1）+1；2、LCS（Xm-1，Y），LCS（X，Yn-1）；3、max{LCS（Xm-1，Y），LCS（X，Yn-1）}。

<img src="https://github.com/Choven-Meng/Python_Algorithms/blob/master/photo/lcs.png" width="25%" height="25%" />

<img src="https://github.com/Choven-Meng/Python_Algorithms/blob/master/photo/lcs_run.png" width="25%" height="25%" />

上图是运行结果，第一个矩阵是计算公共子序列长度的，可以看到最长是4；第二个矩阵是构造这个最优解用的；最后输出一个最优解BCBA。
