#include<cstdio>
#include<iostream>
#define ll long long
using namespace std;
ll n,q,x,y,s[10000010],zhi[10000010],pin;
void pri(ll x);
ll chai(ll x);
ll gcd(ll x,ll y);
int main()
{
	scanf("%lld%lld",&n,&q);
	for(ll i = 2; i <= n; i++)
	{
		pri(i);
	}
	for(ll i = 1; i <= q; i++)
	{

		scanf("%lld%lld",&x,&y);
		if(x==y)
		{
			printf("0\n");
		}
		else
		{
			printf("%lld\n",chai(x / gcd(x,y)));
		}
	}
	return 0;
}
ll gcd(ll x,ll y)
{
	while(y)
	{
		ll t = y;
		y = x % y;
		x = t;
	}
	return x;
}
void pri(ll x)
{
	if(!s[x])
	{
		zhi[pin++] = x;
		for(ll i = 2; i * x <= n; i++)
		{
			s[i * x] = 1;
		}
	}
}
ll chai(ll x)
{
	ll ans = 0;
	if(x==1)
	{
		ans++;
	}
	for(int i = 0; i < pin; i++)
	{
		while(x % zhi[i] == 0&&x != 1)
		{
			ans += zhi[i];
			x /= zhi[i];
		}
		if(x == 1) break;
	}
	return ans;
}