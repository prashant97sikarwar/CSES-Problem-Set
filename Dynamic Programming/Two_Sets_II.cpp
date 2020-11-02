#include<iostream>
#include<bits/stdc++.h>
using namespace std;
const int MOD = 1000000007;
#define ll long long int

int solve(int n){
    int total = n*(n+1)/2;
    if (total%2 == 1)
        return 0;
    int sm = total / 2;
    long long int dp[n+1][sm+1];
    for(int i=0;i<=n;i++){
        for(int j=0;j<=sm;j++){
            dp[i][j] = 0;
        }
    }
    dp[0][0] = 1;
    for(int i=0;i<=n;i++){
        dp[i][0] = 1;
    }
    for(int i=1;i<n+1;i++){
        for(int j=1;j<sm+1;j++){
            if (j >= i)
                dp[i][j] = (dp[i-1][j-i]%MOD + dp[i-1][j]%MOD)%MOD;
            else
                dp[i][j] = dp[i-1][j]%MOD;
        }
    }
    
    ll ans = (dp[n][sm] * 500000004) %MOD;
    return ans;
}

int main(){
    int n;
    cin >> n;
    cout << solve(n) <<'\n';
    return 0;
}