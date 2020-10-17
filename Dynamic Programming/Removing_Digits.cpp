#include<iostream>
#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ll n;
    cin >> n;
    vector<ll> dp(n+1);
    dp[0] = 0;
    for(int i=1;i<=n;i++){
        int temp = i;
        dp[i] = 1e6+2;
        while (temp > 0){
            int rem = temp % 10;
            if (rem == 0){
                temp /=10;
                continue;
            }
            dp[i] = min(1 + dp[i-rem],dp[i]);
            temp /= 10;
        }
    }
    cout << dp[n] <<'\n';
    return 0;
}

