// Problem Link :- https://cses.fi/problemset/task/1634

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

#define ll long long
const int MOD = 1000000007;
int main(){
    ll n,x;
    cin >> n >> x;
	vector<ll> v(n);
	for(ll i=0;i<n;i++){
	    cin >> v[i];
	}
    ll dp[x+1] = {x+1};
    for(int i=0;i<x+1;i++){
        dp[i] = x+1;
    }
    dp[0] = 0;
    sort(v.begin(), v.end());
    for(int i=0;i<n;i++){
        for(ll j=1;j<x+1;j++){
            if (j >= v[i])
                dp[j] = std::min(1+dp[j-v[i]],dp[j]);
        }
    }
    if (dp[x] < x+1)
        cout << dp[x] << '\n';
    else
        cout << -1 << '\n';
        
    return 0;
}
