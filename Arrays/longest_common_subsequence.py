#Longest common subsequence
# The longest common subsequence (LCS) problem is the problem of finding the longest subsequence common to all sequences in a set of sequences (often just two sequences). It differs from the longest common substring problem: unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences. The longest common subsequence problem is a classic computer science problem, the basis of data comparison programs such as the diff utility, and has applications in computational linguistics and bioinformatics. It is also widely used by revision control systems such as Git for reconciling multiple changes made to a revision-controlled collection of files.
# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem


def lcs(s1,s2,memo):

    if (s1,s2) in memo:
        return memo[(s1,s2)]

    if s1 == "" or s2 == "":
        memo[(s1,s2)] = 0
        return 0

    elif s1[0] == s2[0]:
        memo[(s1,s2)] = 1 + lcs(s1[1:], s2[1:],memo)
        return memo[s1,s2]

    else:
        memo[(s1,s2)] = max(lcs(s1[1:], s2, memo), lcs(s1,s2[1:],memo))
        return memo[(s1,s2)]


if __name__ == "__main__":
    memo = {}
    print (lcs("abcooooop", "aicsqq", memo))
    print (memo)