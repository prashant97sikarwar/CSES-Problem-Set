#include<iostream>
#include<bits/stdc++.h>
using namespace std;
#define ll long long int
const int MOD = 1000000007;

int main(){
    ll n,x;
    cin >> n >> x;
    vector<int> prices(n);
    vector<int> pages(n);
    for(ll i=0;i<n;i++){
        cin >> prices[i];
    }
    for(ll i=0;i<n;i++){
        cin >> pages[i];
    }
    ll dp[n+1][x+1];
    for(ll i=0;i<n+1;i++){
        for(ll j=0;j<x+1;j++){
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            else if (j >= prices[i-1])
                dp[i][j] = max(dp[i-1][j],pages[i-1] + dp[i-1][j-prices[i-1]]);
            else
                dp[i][j] = dp[i-1][j];
            
        }
    }
    cout << dp[n][x] <<'\n';
    return 0;
}
