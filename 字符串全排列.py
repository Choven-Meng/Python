
"""
输入一个字符串，打印这个字符串中字符的全排列。 
eg： 
输入：abc 
输出：abc acb bac bca cab cba 
"""


def perm(s=''):
    if len(s) <= 1:
        return [s]
    sl = []
    for i in range(len(s)):
        for j in perm(s[0:i] + s[i + 1:]):
            sl.append(s[i] + j)
    return sl
