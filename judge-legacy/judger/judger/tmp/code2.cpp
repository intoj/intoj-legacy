#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include <iostream>
using namespace std;

#define AC
// #define RE
// #define MLE
// #define WA

#ifdef MLE
int a[20900000];
int c[20900000];
int main(){
	cout << sizeof(a)/1024/1024 << endl;
	memset(c,0,sizeof c);
	a[1] = 0;
	c[3] = -233;
	for( int i = 4 ; i <= 10000010 ; i++ ){
		a[i] = c[i-2] + a[i-1];
		c[i] = a[i-3] + a[i-2] + c[i-1];
		if( i == 999999 ) cout << a[10] << endl;
	}
	cout << c[10000000] <<  " " << a[233] << endl;
	//while(1);
	return 0;
}
#endif

#ifdef RE
int Re(){
	int a,b,c;
	Re();
}
int main(){
	Re();
}
#endif

#ifdef AC
int main(){
	int a,b;
	cin >> a >> b;
	cout << a+b << endl;
	return 0;
}
#endif

#ifdef WA
int main(){
	int g = 1;
	for( long long i = 1 ; i <= 2000000000LL ; i++ )
		g <<= 1LL;
	int a,b;
	cin >> a >> b;
	cout << a+b+233+g << endl;
	return 0;
}
#endif
