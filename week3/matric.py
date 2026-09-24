def lcs_length(X,Y):
    m,n=len(X),len(Y)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if X[i]==Y[j]:
                dp[i+1][j+1]=dp[i][j]+1
            else:
                dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
    return dp[m][n]
s1="I am gay AB"
s2="ABCDF"
length=lcs_length(s1,s2)
print(f"longest common subsequence length between '{s1}' and '{s2}' is {length}")