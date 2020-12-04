//Problem Link:- https://cses.fi/problemset/task/1192

#include<bits/stdc++.h>
using namespace std;

char arr[1001][1001];
bool vis[1001][1001];
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
int n,m;

bool isvalid(int x,int y){
    if (x < 1 || y < 1 || x > n || y > m)
        return false;
    if (vis[x][y] == true || arr[x][y] == '#')
        return false;
    return true;
}

void dfs(int x, int y){
    vis[x][y] = true;
    for(int i=0;i<4;i++){
        if (isvalid(x+dx[i],y+dy[i]))
            dfs(x+dx[i],y+dy[i]);
    }
}

int main(){
    cin >> n >> m;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            cin >> arr[i][j];
        }
    }
    int cc = 0;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            if (arr[i][j] == '.' && vis[i][j] == false){
                dfs(i,j);
                cc++;
            }
        }
    }
    cout << cc;
}