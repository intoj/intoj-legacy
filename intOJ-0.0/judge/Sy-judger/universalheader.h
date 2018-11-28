#ifndef UNIVERSALHEADER
#define UNIVERSALHEADER

#define CERR 0

#include <bits/stdc++.h>
using namespace std;
#define Fin(a) freopen(a,"r",stdin);
#define O(a) cout << #a << " " << a << endl;
#define B cout << "Breakpoint!" << endl;
int System( string a ){
	return system(a.c_str());
}
void End(){
	//System("rm -rf temp/");
	exit(0);
}
bool Exist( string path ){
	System("([ -f "+path+" ] && echo 1 || echo 0) > temp/sysreturn.txt");
	Fin("sysreturn.txt");
	int a; cin >> a;
	return a;
}
string itoa( int a ){
	string s;
	while(a){
		s += a%10 + '0';
		a /= 10;
	}
	reverse(s.begin(),s.end());
	return s;
}
#include "log.cpp"
#include "status.cpp"
#include "init.cpp"
#include "judge.cpp"

#endif
