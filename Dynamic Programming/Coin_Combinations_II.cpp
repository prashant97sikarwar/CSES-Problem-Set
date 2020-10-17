//Problem Link:- https://cses.fi/problemset/task/1636

#include <iostream>
#include<vector>
#include <algorithm>
using namespace std;
#define ll long long
const int MOD = 1000000007;


int main() {
    ll n,x;
    cin >> n >> x;
	vector<ll> v(n);
	for(ll i=0;i<n;i++){
	    cin >> v[i];
	}
	ll dp[x+1] = {0};
	dp[0] = 1;
	sort(v.begin(), v.end()); 
	for(ll i=0;i<n;i++){
	    for(ll j=1;j<=x;j++){
	        if (v[i] <= j){
	            dp[j] += (dp[j-v[i]])%MOD;
	            dp[j] %= MOD;
	        }
	    }
	}
	cout << dp[x] <<'\n';
	return 0;
}
