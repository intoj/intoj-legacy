#include <bits/stdc++.h>
using namespace std;
int system( string s ){
	return system(s.c_str());
}

int pid,tlim,mlim,ctlim,cmlim;
ifstream config;
ofstream result,message;

void Comp(){
	int compcode = system("g++ -DONLINE_JUDGE code.cpp -o code -lm -w -fmax-errors=5 2> compres.txt");
	if( compcode != 0 ){
		result << "Compile Error" << endl;
		ifstream compres;
		compres.open("compres.txt",ios::in);
		string s;
		while( getline(compres,s) ) message << s << endl;
		exit(0);
	}
}

void Run(){
	int ret = system("./run.sh");
	cout << ret << endl;
	cout << bitset<32>(ret) << endl;
}

int main(){
	config.open("judgeconf.txt",ios::in);
	result.open("judgeresult.txt",ios::out);
	message.open("judgemessage.txt",ios::out);
	config >> pid >> tlim >> mlim >> ctlim >> cmlim;
	Comp();
	Run();
}
