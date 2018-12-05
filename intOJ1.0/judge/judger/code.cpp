
#include <bits/stdc++.h>
using namespace std;

int a[100];
int main(){
	for( int i = 1 ; i <= 50 ; i++ )
		cout << a[i*100] << endl;
}

/*
#include <bits/stdc++.h>
using namespace std;

int n,m;
int a[10000000];
int b[10000000];
long long c[10000000];

int main(){
	for( int i = 1 ; i <= 10000 ; i++ ){
		a[rand()%10000000] = rand();
		b[rand()%10000000] = rand();
		c[rand()%10000000] = rand();
	}
	cout << "ORZ" << " " << a[1] << " " << b[1] << " " << c[1] << endl;
}
*/
