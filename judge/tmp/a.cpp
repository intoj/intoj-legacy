#include <functional>
#include <algorithm>
#include <iostream>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <climits>
#include <iomanip>
#include <bitset>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <ctime>
#include <set>
#include <map>
using namespace std;
#define il inline
#define rg register
#define elif else if

// Type
#define ld double
#define ll long long
#define ull unsigned ll

// Vector
#define vc vector
#define Pb push_back
#define Pf push_front
#define All(x) x.begin(),x.end()

// Memory
#define Ms(_data) memset(_data,0,sizeof(_data))
#define Msn(_data,_num) memset(_data,_num,sizeof(_data))

// Template
#define _cl class
#define _tp template
#define _tyn typename

// Pair
#define Mp make_pair
#define F first
#define S second
#define pii pair<int,int>
#define pli pair<ll,int>
#define pil pair<int,ll>
#define pll pair<ll,ll>

// File
#define Fin(a) freopen(a,"r",stdin)
#define Fout(a) freopen(a,"w",stdout)
il void FILEIO(){
	#ifdef intLSY
		Fin("in.in");
	#endif
}
il void FILEIO( string pname ){
	Fin((pname+".in").c_str());
	#ifndef intLSY
		Fout((pname+".out").c_str());
	#endif
}
void Printtime(){
	#ifdef intLSY
		double _timeuse = clock()* 1000.0 / CLOCKS_PER_SEC;
		printf("\n\nTime usage:\n%.0lf ms\n",_timeuse);
	#endif
}
void END(){ Printtime(); exit(0); }
_tp<_tyn T>void END( T mes ){ cout << mes << endl; END(); }


// Loop
#define For(i,j) for( rg int (i) = 1 ; (i) <= (j) ; ++(i) )
#define For0(i,j) for( rg int (i) = 0 ; (i) < (j) ; ++(i) )
#define Forx(i,j,k) for( rg int (i) = (j) ; (i) <= (k) ; ++(i) )
#define Forstep(i,j,k,st) for( rg int (i) = (j) ; (i) <= (k) ; (i) += (st) )
#define fOR(i,j) for( rg int (i) = (j) ; (i) >= 1 ; --(i) )
#define fOR0(i,j) for( rg int (i) = (j)-1 ; (i) >= 0 ; --(i) )
#define fORx(i,j,k) for( rg int (i) = (k) ; (i) >= (j) ; --(i) )


// Debug
#define B cout << "BreakPoint" << endl;
#define O(x) cout << #x << " " << x << endl;
#define O_(x) cout << #x << " " << x << "  ";
#define ERR(x) cout << "ERR! #" << x << endl;
#define Msz(x) cout << "Sizeof " << #x << " " << sizeof(x)/1024/1024 << " MB" << endl;
using namespace std;
_tp<_tyn T>void Print( T _a[] , int _s , int _t , char sp = ' ' , char ed = '\n' ){
	for( int i = _s ; i <= _t ; i++ )
		cout << _a[i] << sp;
	cout << ed;
	cout.flush();
}


// Optimize
#define abs(a) ((a)<0?(~(a)+1):(a))
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
//#define swap(a,b) {a=a^b;b=a^b;a=a^b;}
#define Mymax(a,b) (a) = max((a),(b))
#define Mymin(a,b) (a) = min((a),(b))
#define INF (0x3f3f3f3f)
#define LINF ((long long)(0x3f3f3f3f3f3f3f3f))
#define MOD 998244353LL
#define Rmoi(a,b) ((a)%b+b)%b
#define Rmo(a) ((a)%MOD+MOD)%MOD
#define Rmod(a) a = (a%MOD+MOD)%MOD
#define Rmodi(a,b) a = (a%(b)+(b))%(b)
#define Mymoi(a,b) ((a)>=b?((a)-b):(a))
#define Mymo(a) ((a)>=MOD?((a)-MOD):(a))
#define Mymod(a) a = (a)>=MOD?((a)-MOD):(a)
#define Mymodi(a,b) a = ((a)>=(b))?((a)-(b)):(a)
#define INF (0x3f3f3f3f)
#define LINF ((ll)(0x3f3f3f3f3f3f3f3f))
_tp<_tyn T>T Gcd( T a , T b ){ return b?Gcd(b,a%b):a; }
ll Pow( rg ll a , rg ll b , rg ll p = MOD ){
	rg ll ret = 1;
	for( ; b ; a = a*a%p, b >>= 1LL )
		if(b&1LL) ret = ret*a%p;
	return ret;
}
ll Inv( ll a , ll p = MOD ){ return Pow(a,p-2LL); }
///////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////
#define MAXN 16
il int Tran( rg char c ){
	if( c >= '4' && c <= '9' ) return c - '4' + 1;
	if( c == 'T' ) return 7;
	if( c == 'J' ) return 8;
	if( c == 'Q' ) return 9;
	if( c == 'K' ) return 10;
	if( c == 'A' ) return 11;
	if( c == '2' ) return 12;
	if( c == 'w' ) return 13;
	if( c == 'W' ) return 14;
	ERR("[Tran] char not found");
}

const int tot[] = {-1000,4,4,4,4,4,4,4,4,4,4,4,4,1,1};
int wy[MAXN], jrycan[MAXN], jry[MAXN];
int ans;

il void Init(){
	Ms(wy);
	memcpy(jrycan,tot,sizeof tot);
	ans = 0;
}

int Solve(){

	return 1;
}

void Dfs( int pos , int selected ){
	if( selected == 17 ){
		ans += Solve();
		return;
	}
	if( pos > 14 ) return;
	Forx(i,0,jrycan[pos]){
		if( i+selected > 17 ) continue;
		jry[pos] = i;
		Dfs(pos+1,i+selected);
	}
}

int main(){
	FILEIO();

	char s[20];
	while(~scanf("%s",s)){
		Init();
		For0(i,17){
			++wy[Tran(s[i])];
			--jrycan[Tran(s[i])];
		}
		// Print(jrycan,1,14);
		Dfs(1,0);
		printf("%lld\n",ans);
	}

	END();
}
