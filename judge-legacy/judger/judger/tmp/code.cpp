#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>
#include <iostream>
#define rep(i,a,n) for(int i = a;i <= n;++i)
using namespace std;
typedef long long ll;
typedef double D;
const D PI = acos(-1);
int read() {
    int as = 0,fu = 1;
    char c = getchar();
    while(c < '0' || c > '9') {
        if(c == '-') fu = -1;
        c = getchar();
    }
    while(c >= '0' && c <= '9') {
        as = as * 10 + c - '0';
        c = getchar();
    }
    return as * fu;
}
//head
const int N = 50000005;
bool mindiv[N];
int prim[N],phi[N];
ll s[N],ans;
void siere(int n) {
	phi[1] = 1;
	rep(i,2,n) {
		if(!mindiv[i]) prim[++prim[0]] = i,phi[i] = i-1;
		for(int j = 1;i * prim[j] <= n;++j) {
			mindiv[i * prim[j]] = 1;
			if(!(i % prim[j])) {
				phi[i * prim[j]] = phi[i] * prim[j];
				break;
			}
			phi[i * prim[j]] = phi[i] * (prim[j] - 1);
		}
	}
	rep(i,1,n) s[i] = s[i-1] + phi[i];
}
int main() {
	cout << sizeof(prim)/1024/1024 << endl;
	int n = read(),m = read();
	if(n > m) swap(n,m);
	siere(m);
	for(int l = 1,r;l <= n;l = r+1) {
		r = min(n/(n/l),m/(m/l));
		ans += (s[r] - s[l-1]) * (n/l) * (m/l);
	}
	printf("%lld\n",(ans << 1) - 1ll * n * m);
}
