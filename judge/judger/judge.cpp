#include <bits/stdc++.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/syscall.h>
#include <sys/wait.h>
#include <sys/time.h>
#include <pthread.h>
#include <unistd.h>
#include <errno.h>
#define rg register
#define ll long long
#define Pb push_back
using namespace std;
#define For(i,n) for( int i = 1 ; i <= n ; i++ )
#define For0(i,n) for( int i = 0 ; i < n ; i++ )
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
char cmd[233];
#define MAXTESTCASE 1000
int ReadNumber( string a ){
	int ans = 0;
	int len = a.length();
	For0(i,len)
		if(isdigit(a[i]))
			ans = ans*10 + a[i]-'0';
	return ans;
}
bool CompareByNumber( string a , string b ){
	int numa = ReadNumber(a);
	int numb = ReadNumber(b);
	if( numa != numb ) return numa < numb;
	return a.length() < b.length();
}
map<string,int> priority;
bool CompareByPriority( string a , string b ){
	assert(priority.count(a));
	assert(priority.count(b));
	return priority[a] < priority[b];
}
void InitPriority(){
	priority["Compile Error"] = 0;
	priority["Wrong Answer"] = 1;
	priority["Time Limit Exceed"] = 2;
	priority["Memory Limit Exceed"] = 3;
	priority["Runtime Error"] = 4;
	priority["Accepted"] = 100;
}

int testcasecnt;
int problemid,timelimit, memorylimit;
int comptimelimit = 4000, compmemorylimit = 256;
void ReadConfig(){
	ifstream configin;
	configin.open("tmp/config.txt",ios::in);
	configin >> problemid >> timelimit >> memorylimit;
}
void WriteConfig( string inputname , string outputname , int point ){
	ofstream configout;
	configout.open("judger/tmp/config.txt");
	configout << problemid << " " << timelimit << " " << memorylimit << " ";
	configout << comptimelimit << " " << compmemorylimit << " " << point << endl;
	configout << inputname << " " << outputname << endl;
	configout.close();
}
void GetTestcaseCount(){
	sprintf(cmd,"ls -l ../testdata/%d|grep \"^-\"|wc -l > tmp/testcasecnt.txt",problemid); system(cmd);
	ifstream testcasecntin;
	testcasecntin.open("tmp/testcasecnt.txt",ios::in);
	testcasecntin >> testcasecnt;
}
string name[MAXTESTCASE];
void GetTestcaseName(){
	sprintf(cmd,"ls  ../testdata/%d > tmp/testcasename.txt",problemid); system(cmd);
	ifstream testcasenamein;
	testcasenamein.open("tmp/testcasename.txt",ios::in);
	For(i,testcasecnt) testcasenamein >> name[i];
	sort(name+1,name+1+testcasecnt,CompareByNumber);
	//For(i,testcasecnt) cout << name[i] << endl;
}



void InnerBox( bool compile ){
	sprintf(cmd,"cd judger/judger && ./main %d",compile); system(cmd);
}
ifstream resultin;
ofstream resultout;
string status;
int point,timeusage,memoryusage;
vector<string> allstatus;
void ReadResult(){
	resultin.open("judger/result/result.txt",ios::in);
	getline(resultin,status);
	resultin >> point >> timeusage >> memoryusage;
	resultin.close();
}
void WriteResult(){
	resultout << status << endl;
	resultout << point << " " << timeusage << " " << memoryusage << endl;
}
void AllCompileError(){
	For(i,(testcasecnt>>1)+1){
		resultout << "Compile Error" << endl;
		resultout << "0 0 0" << endl;
	}
	exit(0);
}


string finalstatus;
int totpoint,tottimeusage,maxmemoryusage;
void Collect(){
	allstatus.Pb(status);
	totpoint += point;
	tottimeusage += timeusage;
	maxmemoryusage = max(maxmemoryusage,memoryusage);
}
void GetFinalstatus(){
	sort(allstatus.begin(),allstatus.end(),CompareByPriority);
	finalstatus = allstatus[0];
}
void Judge(){
	for( int i = 1 ; i <= testcasecnt ; i += 2 ){
		WriteConfig(name[i],name[i+1],100/(testcasecnt/2));
		InnerBox(i==1);
		ReadResult();
		if( i == 1 && status == "Compile Error" ){
			AllCompileError();
		}
		WriteResult();
		Collect();
		usleep(1000);
	}
	GetFinalstatus();
	resultout << finalstatus << endl;
	resultout << totpoint << " " << tottimeusage << " " << maxmemoryusage << endl;
}


int main(){
	InitPriority();
	resultout.open("result/result.txt",ios::out);
	ReadConfig();
	GetTestcaseCount();
	GetTestcaseName();
	Judge();
	return 0;
}
