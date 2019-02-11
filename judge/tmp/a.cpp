#include <bits/stdc++.h>
using namespace std;

void RE(){ RE(); }

int main(){
srand(time(0));
int a = 1;
for( long long i = 1 ; i <= 2200000000LL ; i++ ) a <<= 1;
int b = rand();
if( b%4 == 1 ) cout << a << endl;
if( b%4 == 2 ) RE();
return 0;
}