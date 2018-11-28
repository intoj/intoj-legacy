#include "universalheader.h"
#ifndef INIT
#define INIT

namespace Init{

void About(){
	cout << "Sy-judger" << endl;
	cout << "By InterestingLSY" << endl;
	cout << "------------------------------" << endl;
}
void Init(){
	System("rm -rf temp/");
	About();
	Log::Init();
	Status::Init();
}

}

#endif
