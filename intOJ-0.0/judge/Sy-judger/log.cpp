#include "universalheader.h"
#ifndef LOG
#define LOG

namespace Log{

ofstream logout;
void Log( string type , string information ){//cout << 233 << endl;
	(!CERR?logout:cerr) << type << ":\t" << information << endl;
	if( type == "Error" ) End();
}
void Init(){
	logout.open("judgerlog.txt");
	Log("Start!","Wish you good luck&high score!");
}

}

#endif
