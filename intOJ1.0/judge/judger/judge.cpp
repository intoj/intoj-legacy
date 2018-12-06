#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;
#define O(a) cout << #a << " " << a << endl
int system( string s ){
	return system(s.c_str());
}
string Tostring( int a ){
	string s;
	while(a){
		s += a%10 + '0';
		a /= 10;
	}
	reverse(s.begin(),s.end());
	return s;
}

int pid,tlim,mlim,ctlim,cmlim;
ifstream config;
ofstream result,message;

void Compile_Error(){
	result << "Compile Error" << endl;
	ifstream compres;
	compres.open("compres.txt",ios::in);
	string s;
	while( getline(compres,s) ) message << s << endl;
	exit(0);
}
void Time_Limit_Exceed(){
	result << "Time Limit Exceed" << endl;
	exit(0);
}
void Memory_Limit_Exceed(){
	result << "Memory_Limit_Exceed" << endl;
	exit(0);
}


void Comp(){
	int compcode = system("g++ -DONLINE_JUDGE code.cpp -o code -lm -w -fmax-errors=5 2> compres.txt");
	if( compcode != 0 ){
		Compile_Error();
	}
}

ifstream processid,memfile;
int proid,memusage;
void Run(){
	auto id = fork();
	if( id == 0 ){
		system("./code > ans.out");
	}else{
		mlim *= 1024;
		usleep(500);
		system("pidof code > pid.txt");
		processid.open("pid.txt",ios::in);
		processid >> proid;
		auto st = clock(), ed = clock();
		while( (ed-st)*1000/CLOCKS_PER_SEC <= tlim ){
			ed = clock();
			system("memstat > mem.txt");
			memfile.open("mem.txt",ios::in);
			memfile >> memusage;
			O(memusage);
			O((ed-st)*1000/CLOCKS_PER_SEC);
			if( memusage > mlim ) Memory_Limit_Exceed();
			memfile.close();
			usleep(10000);
		}
		if( (ed-st)*1000/CLOCKS_PER_SEC > tlim ){
			system("kill "+Tostring(proid));
			Time_Limit_Exceed();
		}
	}
}

int main(){
	config.open("judgeconf.txt",ios::in);
	result.open("judgeresult.txt",ios::out);
	message.open("judgemessage.txt",ios::out);
	config >> pid >> tlim >> mlim >> ctlim >> cmlim;
	cout << "Compiling..." << endl;
	Comp();
	cout << "Runnning..." << endl;
	Run();
	return 0;
}
