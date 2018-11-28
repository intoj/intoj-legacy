#include "universalheader.h"

int main( int argc , char **argv ){
	argc--;
	Init::Init();
	if( argc != 0 && argc != 3 ){
		Log::Log("Error",(string)"Invaild Command: " + char(argc+'0') + " args is given");
	}
	if( argc != 3 ){
		Log::Log("Warning","Using (source/?.cpp) (source/?.in) (source/?.out)");
	}

	string propath = argc?argv[1]:"source/*.cpp";
	string inpath = argc?argv[2]:"source/*.in";
	string outpath = argc?argv[3]:"source/*.out";
	System("mkdir temp");

	Log::Log("Notice","Propath:"+propath);
	Log::Log("Notice","Inpath:"+inpath);
	Log::Log("Notice","Outpath:"+outpath);
	if(!Exist(propath)) Log::Log("Error","Program does not exist");
	if(!Exist(inpath)) Log::Log("Error","Infile does not exist");
	if(!Exist(outpath)) Log::Log("Error","Outfile does not exist");
	System("cp "+propath+" temp/pro.cpp");
	System("cp "+inpath+" temp/data.in");
	System("cp "+outpath+" temp/data.out");

	Judge::Compile();
	Judge::Run();
	Judge::Diff();
	Judge::Accept();

	return 0;
}
