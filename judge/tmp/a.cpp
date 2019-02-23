#include <bits/stdc++.h>
using namespace std;
#define For(i,j) for( int (i) = 1 ; (i) <= (j) ; ++(i) )
#define Forx(i,a,b) for( int (i) = (a) ; (i) <= (b) ; ++(i) )
#define ld double

#define MAXN 101000
#define Eps 1e-9
inline bool Cmp( ld a , ld b ){ return a > b; }

int n,k;
int a[MAXN], b[MAXN];

ld p[MAXN];
bool Check( ld ans ){
	For(i,n) p[i] = a[i] - b[i]*ans;
	nth_element(p+1,p+k+1,p+n+1,Cmp);
	ld sum = 0;
	For(i,k) sum += p[i];
	return sum >= 0;
}
// OOOOOOXXXXXX
ld Binarysearch(){
	ld l = 0, r = 1.2, mid, ans = 0;
	while( r-l >= Eps ){
		mid = (l+r)/2;
		if(Check(mid)){//O(mid);
			ans = max(ans,mid);
			l = mid+Eps;
		}else
			r = mid-Eps;
	}
	return ans;
}

int main(){
	scanf("%d%d",&n,&k);
	For(i,n) scanf("%d",a+i);
	For(i,n) scanf("%d",b+i);

	ld ans = Binarysearch();
	printf("%.4lf\n",ans);

	return 0;
}
