def lcs(string1, string2, n, m):
    if n == 0 or m == 0:
        return 0

    elif string1[n - 1] == string2[m - 1]:
        return 1 + lcs(string1, string2, n - 1, m - 1)

    else:
        return max(lcs(string1, string2, n - 1, m), lcs(string1, string2, n, m - 1))


if __name__ == '__main__':
    S1 = "abcdaf"
    S2 = "acbcf"
    print("length of the longest common subsequence is : ", lcs(S1, S2, len(S1), len(S2)))

# The time complexity is O(2^m*n) and the space complexity is O(1)
