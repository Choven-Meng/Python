## 问题描述

什么是最长公共子序列呢?好比一个数列 S，如果分别是两个或多个已知数列的子序列，且是所有符合此条件序列中最长的，则S 称为已知序列的最长公共子序列。

举个例子，如：有两条随机序列，如 1 3 4 5 5 ，and 2 4 5 5 7 6，则它们的最长公共子序列便是：4 5 5。

注意最长公共子串（Longest CommonSubstring）和最长公共子序列（LongestCommon Subsequence, LCS）的区别：子串（Substring）是串的一个连续的部分，子序列（Subsequence）则是从不改变序列的顺序，而从序列中去掉任意的元素而获得的新序列

## 解决思路：动态规划算法

 事实上，最长公共子序列问题也有最优子结构性质。

记:

X<sub>i</sub>=﹤x<sub>1</sub>，⋯，x<sub>i</sub>﹥即X序列的前i个字符 (1≤i≤m)（前缀）

Y<sub>j</sub>=﹤y<sub>1</sub>，⋯，y<sub>j</sub>﹥即Y序列的前j个字符 (1≤j≤n)（前缀）

假定Z=﹤z<sub>1</sub>，⋯，z<sub>k</sub>﹥∈LCS(X , Y)。

  > 若x<sub>m</sub>=y<sub>n</sub>（最后一个字符相同），则不难用反证法证明：该字符必是X与Y的任一最长公共子序列Z（设长度为k）的最后一个字符，即有
  z<sub>k</sub> = x<sub>m</sub> = y<sub>n</sub> 且显然有Z<sub>k</sub>-1∈LCS(X<sub>m</sub>-1 , Y<sub>n</sub>-1),即Z的前缀Z<sub>k</sub>-1是X<sub>m</sub>-1与Y<sub>n</sub>-1的最长公共子序列。此时，问题化归成求X<sub>m</sub>-1与Y<sub>n</sub>-1的LCS（LCS(X , Y)的长度等于LCS(X<sub>m</sub>-1 , Y<sub>n</sub>-1)的长度加1）。

  > 若x<sub>m</sub>≠y<sub>n</sub>，则亦不难用反证法证明：要么Z∈LCS(X<sub>m</sub>-1, Y)，要么Z∈LCS(X , Y<sub>n</sub>-1)。由于z<sub>k</sub> ≠ <sub>m</sub>与z<sub>k</sub> ≠ y<sub>n</sub>其中至少有一个必成立，若z<sub>k</sub> ≠ x<sub>m</sub>则有Z∈LCS(X<sub>m</sub>-1 , Y)，类似的，若z<sub>k</sub> ≠ y<sub>n</sub> 则有Z∈LCS(X , Y<sub>n</sub>-1)。此时，问题化归成求X<sub>m</sub>-1与Y的LCS及X与Y<sub>n</sub>-1的LCS。LCS(X , Y)的长度为：max{LCS(X<sub>m</sub>-1 , Y)的长度, LCS(X , Y<sub>n</sub>-1)的长度}。

  > 由于上述当xm≠yn的情况中，求LCS(Xm-1 , Y)的长度与LCS(X , Yn-1)的长度，这两个问题不是相互独立的：两者都需要求LCS(Xm-1，Yn-1)的长度。另外两个序列的LCS中包含了两个序列的前缀的LCS，故问题具有最优子结构性质考虑用动态规划法。

  > 也就是说，解决这个LCS问题，你要求三个方面的东西：1、LCS（Xm-1，Yn-1）+1；2、LCS（Xm-1，Y），LCS（X，Yn-1）；3、max{LCS（Xm-1，Y），LCS（X，Yn-1）}。

### 最长公共子序列的结构

最长公共子序列的结构有如下表示：

设序列X=<x1, x2, …, xm>和Y=<y1, y2, …, yn>的一个最长公共子序列Z=<z1, z2, …, zk>，则：

> 1.若xm=yn，则zk=xm=yn且Zk-1是Xm-1和Yn-1的最长公共子序列；
> 2.若xm≠yn且zk≠xm ，则Z是Xm-1和Y的最长公共子序列；
> 3.若xm≠yn且zk≠yn ，则Z是X和Yn-1的最长公共子序列。
> 其中Xm-1=<x1, x2, …, xm-1>，Yn-1=<y1, y2, …, yn-1>，Zk-1=<z1, z2, …, zk-1>。

### 子问题的递归结构

 > 由最长公共子序列问题的最优子结构性质可知，要找出X=<x1, x2, …, xm>和Y=<y1, y2, …, yn>的最长公共子序列，可按以下方式递归地进行：当xm=yn时，找出Xm-1和Yn-1的最长公共子序列，然后在其尾部加上xm(=yn)即可得X和Y的一个最长公共子序列。当xm≠yn时，必须解两个子问题，即找出Xm-1和Y的一个最长公共子序列及X和Yn-1的一个最长公共子序列。这两个公共子序列中较长者即为X和Y的一个最长公共子序列。

 > 由此递归结构容易看到最长公共子序列问题具有子问题重叠性质。例如，在计算X和Y的最长公共子序列时，可能要计算出X和Yn-1及Xm-1和Y的最长公共子序列。而这两个子问题都包含一个公共子问题，即计算Xm-1和Yn-1的最长公共子序列。

 > 与矩阵连乘积最优计算次序问题类似，我们来建立子问题的最优值的递归关系。用c[i,j]记录序列Xi和Yj的最长公共子序列的长度。其中Xi=<x1, x2, …, xi>，Yj=<y1, y2, …, yj>。当i=0或j=0时，空序列是Xi和Yj的最长公共子序列，故c[i,j]=0。其他情况下，由定理可建立递归关系如下：

    if i = 0 or j = 0 ,c[i,j] = 0;  
    if i,j > 0 and $$ x_i $$ == $$ y_i $$ , c[i,j] = c[i-1,j-1]+1;  
    if i,j > 0 and $$ x_i $$ != $$ y_i $$ , c[i,j] = max(c[i,j-1],c[i-1,j])
    
由算法LCS计算得到的数组L可用于快速构造序列X=<x1, x2, …, xm>和Y=<y1, y2, …, yn>的最长公共子序列。首先从L[i,j]开始，沿着其中的箭头所指的方向在数组L中搜索。  


 <img src="https://github.com/Choven-Meng/Python_Algorithms/blob/master/photo/lcs.png" width="25%" height="25%" />  


* 当L[i,j]中遇到"↖"时（意味着xi=yi是LCS的一个元素），表示Xi与Yj的最长公共子序列是由Xi-1与Yj-1的最长公共子序列在尾部加上xi得到的子序列；

* 当L[i,j]中遇到"↑"时，表示Xi与Yj的最长公共子序列和Xi-1与Yj的最长公共子序列相同；

* 当b[i,j]中遇到"←"时，表示Xi与Yj的最长公共子序列和Xi与Yj-1的最长公共子序列相同。



<img src="https://github.com/Choven-Meng/Python_Algorithms/blob/master/photo/lcs_run.png" width="25%" height="25%" />

上图是运行结果，第一个矩阵是计算公共子序列长度的，可以看到最长是4；第二个矩阵是构造这个最优解用的；最后输出一个最优解BCBA。
