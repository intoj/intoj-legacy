#include "universalheader.h"
#ifndef JUDGE
#define JUDGE

// -a -q -B -b

namespace Judge{

void Compile(){
	int fail = System("g++ temp/pro.cpp -o temp/pro");
	if(fail) Status::Status("CompileError",-1,-1,"");
}
void Run(){
	int returnval = System("./temp/pro <temp/data.in >temp/pro.out");
	(returnval >>= 8)  &= 0x0F;
	if( returnval != 0 ){
		Status::Status("RuntimeError",-1,-1,"Signal:"+itoa(returnval));
	}
}
void Diff(){
	System("diff temp/data.out temp/pro.out -a -B -b -d --suppress-common-lines > temp/diff.txt");
	Fin("temp/diff.txt");
	cin.clear();
	string s;
	if( cin >> s ){
		string mes;
		getline(cin,s);
		getline(cin,s);
		s = s.substr(2,100);
		mes += s+" expected but ";
		getline(cin,s);
		getline(cin,s);
		s = s.substr(2,100);
		mes += s+" found.QwQ";
		Status::Status("WrongAnswer",clock()/1000,-1,mes);
	}
}
void Accept(){
	Status::Status("Accept",clock()/1000,-1,"=w=");
}

}

#endif
