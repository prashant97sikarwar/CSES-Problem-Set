#include<iostream>
#include<bits/stdc++.h>
using namespace std;
#define ll long long

bool com(int a,int b){
    return (a < b);
}

int solve(string str1, string str2){
    int n = str1.length();
    int m = str2.length();
    int dp[n+1][m+1];
    for(int i=0;i<=n;i++){
        for(int j=0;j<=m;j++){
            if (i==0)
                dp[i][j] = j;
            else if (j == 0)
                dp[i][j] = i;
            else if (str1[i-1] == str2[j-1])
                dp[i][j] = dp[i-1][j-1];
            else
            {
                dp[i][j] = 1 + min({dp[i][j-1],dp[i-1][j-1],dp[i-1][j]},com);
            }
        }
    }
    return dp[n][m];
}

int main(){
    string str1,str2;
    cin >> str1;
    cin >> str2;
    cout << solve(str1,str2) << '\n';
    return 0;
}