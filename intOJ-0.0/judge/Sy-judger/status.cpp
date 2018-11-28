#include "universalheader.h"
#ifndef STATUS
#define STATUS

namespace Status{

ofstream status;
void Status( string s , int timeuse , int memuse , string discription ){
	status << s << " " << (timeuse!=-1?itoa(timeuse):"N/A") << " " << (memuse!=-1?itoa(memuse):"N/A") << " " << discription << endl;
	End();
}
void Init(){
	status.open("status.txt");
}

}

#endif
