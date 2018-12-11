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
using namespace std;
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



int problemid,timelimit,memorylimit,comptimelimit,compmemorylimit,fullscore;
char inputfilename[233], outputfilename[233];
int timeusage, memoryusage;
void ReadConfigFile(){
	ifstream configin;
	configin.open("../tmp/config.txt",ios::in);
	configin >> problemid >> timelimit >> memorylimit >> comptimelimit >> compmemorylimit >> fullscore;
	configin >> inputfilename >> outputfilename;
}
ofstream resultout,messageout,compileresultout;
void OpenOutputFile(){
	resultout.open("../result/result.txt",ios::out);
	messageout.open("../result/message.txt",ios::out);
	compileresultout.open("../result/compileresult.txt",ios::out);
}
void WriteConfig(){
	sprintf(cmd,"echo %dM > /sys/fs/cgroup/memory/intoj-run/memory.limit_in_bytes",memorylimit); system(cmd);
	sprintf(cmd,"echo %dM > /sys/fs/cgroup/memory/intoj-run/memory.memsw.limit_in_bytes",memorylimit); system(cmd);
	sprintf(cmd,"echo \"233\" > /sys/fs/cgroup/memory/intoj-run/memory.memsw.max_usage_in_bytes"); system(cmd);
}



void CompileError(){
	resultout << "Compile Error" << endl;
	resultout << "0 0 0" << endl;
	ifstream compileresultin;
	compileresultin.open("../tmp/compres.txt",ios::in);
	string s;
	while( getline(compileresultin,s) ) compileresultout << s << endl;
	exit(0);
}
void TimeLimitExceed(){
	resultout << "Time Limit Exceed" << endl;
	resultout << 0 << " " << timeusage << " " << memoryusage << endl;
	exit(0);
}
void MemoryLimitExceed(){
	resultout << "Memory Limit Exceed" << endl;
	resultout << 0 << " " << timeusage << " " << memoryusage << endl;
	exit(0);
}
void RuntimeError( string message ){
	resultout << "Runtime Error" << endl;
	resultout << "0 0 0" << endl;
	messageout << message << endl;
	exit(0);
}
void WrongAnswer( string message = " " ){
	resultout << "Wrong Answer" << endl;
	resultout << 0 << " " << timeusage << " " << memoryusage << endl;
	messageout << message << endl;
	exit(0);
}
void Accepted(){
	resultout << "Accepted" << endl;
	resultout << fullscore << " " << timeusage << " " << memoryusage << endl;
	exit(0);
}




void ReadMemoryUsage(){
	ifstream memusagein;
	memusagein.open("/sys/fs/cgroup/memory/intoj-run/memory.memsw.max_usage_in_bytes",ios::in);
	memusagein >> memoryusage;
	memoryusage /= 1024*1024;
}

void Compile(){
	cout << "Compiling..." << endl;
	int state = system("g++ -DONLINE_JUDGE ../tmp/code.cpp -o ../tmp/code -lm -w -fmax-errors=5 2> ../tmp/compres.txt");
	if( state != 0 ) CompileError();
}

void RunAsChild(){
	usleep(10000);
	sprintf(cmd,"../tmp/./code < ../../../testdata/%d/%s > ../tmp/ans.txt 2> ../tmp/err.txt",problemid,inputfilename);
	execl("/bin/sh","sh","-c",cmd,(char *)0);
	exit(0);
}
void RunAsFather( int childpid ){
	sprintf(cmd,"echo %d > /sys/fs/cgroup/memory/intoj-run/tasks",childpid); system(cmd);
	int status;
	rg struct timeval starttimeval,nowtimeval;
	timelimit *= 1000;
	gettimeofday(&starttimeval,NULL);
	rg ll starttime = 1LL*starttimeval.tv_sec*1000000+starttimeval.tv_usec;

	while(waitpid(childpid,&status,WNOHANG)==0){
		usleep(3000);
		gettimeofday(&nowtimeval,NULL);
		timeusage = 1LL*nowtimeval.tv_sec*1000000+nowtimeval.tv_usec - starttime;
		if( timeusage > timelimit ){
			timeusage /= 1000;
			TimeLimitExceed();
		}
	}
	timeusage /= 1000;

	ReadMemoryUsage();
	if( memoryusage >= memorylimit || memoryusage == 0 ) MemoryLimitExceed();
	if( status != 0 ){
		string errormessage;
		ifstream errin;
		errin.open("../tmp/err.txt",ios::in);
		getline(errin,errormessage);
		RuntimeError(errormessage);
	}
}
void Run(){
	cout << "Running..." << endl;
	int id = fork();
	if( id == 0 ){
		RunAsChild();
	}else{
		RunAsFather(id);
	}
}

void Judge(){
	sprintf(cmd,"diff -w ../tmp/ans.txt ../../../testdata/%d/%s > ../tmp/diff.txt 2> ../tmp/diff.txt",problemid,outputfilename);
	int ret = system(cmd);
	if( ret == 0 ) Accepted();
	else WrongAnswer();
}

int main( int argc , char **argv ){
	ReadConfigFile();
	OpenOutputFile();
	WriteConfig();

	if( argv[1][0] == '1' ) Compile();
	Run();
	Judge();

	return 0;
}
