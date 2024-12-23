#include<bits/stdc++.h>
using namespace std;
const int N=1e6+10;
int tr[N][27];
int len;
int f[N];
void insert(string s)
{
    int p=0;
    for(int i=0;i<s.size();i++)
    {
        int y=s[i]-'a';
        if(!tr[p][y]) tr[p][y]=++len;
        p=tr[p][y];
    }
    f[p]++;
}
int query(string s)
{
    int p=0;
    int res=0;
    for(int i=0;i<s.size();i++)
    {
        int x=s[i]-'a';
        if(!tr[p][x]) break;
        p=tr[p][x];
        res+=f[p];
    }
    return res;
}
int main()
{
    return query(123);
}