#Longest increasing subsequence

# The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/


import math

def lis(list, start, memo):

    if len(list) == 0:
        return 0

    elif list[0] <= start:
        return lis(list[1:], start, memo)

    else:
        if list[0] in memo:
            a = memo[list[0]]
        else:
            memo[list[0]] = 1+lis(list[1:],list[0], memo)
            a = memo[list[0]]

        return max(a, lis(list[1:], start, memo))


if __name__ == "__main__":
    memo = {}
    print (lis([100,122,10,22,9,33,21,50,41,60,80], -math.inf, memo))
    print (memo)