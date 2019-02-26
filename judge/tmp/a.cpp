#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#define M 200200
using namespace std;
struct abcd{
	int to,next;
}table[M<<1];
int head[M],tot=1;
int n,m,ans,good_cnt,bad_cnt;
int dpt[M],fa[M],good[M],bad[M];
bool v[M];
void Add(int x,int y)
{
	table[++tot].to=y;
	table[tot].next=head[x];
	head[x]=tot;
}
void DFS(int x,int from)
{
	int i;
	v[x]=true;
	dpt[x]=dpt[fa[x]]+1;
	for(i=head[x];i;i=table[i].next)
		if(i^from^1)
		{
			if(!v[table[i].to])
			{
				fa[table[i].to]=x;
				DFS(table[i].to,i);
				good[x]+=good[table[i].to];
				bad[x]+=bad[table[i].to];
			}
			else
			{
				if(dpt[table[i].to]>dpt[x])
					continue;
				if(dpt[x]-dpt[table[i].to]&1)
					good[x]++,good[table[i].to]--,good_cnt++;
				else
					bad[x]++,bad[table[i].to]--,bad_cnt++;
			}
		}
}
int main()
{
	// freopen("voltage.in","r",stdin);
	// freopen("voltage.out","w",stdout);
	int i,x,y;
	cin>>n>>m;
	for(i=1;i<=m;i++)
	{
		scanf("%d%d",&x,&y);
		Add(x,y);
		Add(y,x);
	}
	for(i=1;i<=n;i++)
		if(!v[i])
			DFS(i,0);
	for(i=1;i<=n;i++)
		if(fa[i]&&bad[i]==bad_cnt&&!good[i])
			++ans;
	if(bad_cnt==1)
		++ans;
	cout<<ans<<endl;
}