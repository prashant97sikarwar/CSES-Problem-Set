// Problem Link :- https://cses.fi/problemset/task/1635

#include<iostream>
#include<bits/stdc++.h>
using namespace std;
#define ll long long int
const int MOD = 1000000007;

int main(){
    ll n,x;
    cin >> n >> x;
    vector<ll> arr(n);
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    sort(arr.begin(),arr.end());
    vector<ll> dp(x+1);
    dp[0] = 1;
    for(int j=1;j<=x;j++){
        for(int i=0;i<n;i++){
            if (j >= arr[i]){
                dp[j] += (dp[j-arr[i]])%MOD;
                dp[j] %= MOD;
            }    
        }
    }
    cout << dp[x] <<'\n';
    return 0;
}