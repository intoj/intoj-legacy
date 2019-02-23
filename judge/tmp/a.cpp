#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <string.h>
using namespace std;
 
string BigMul(string s,string t){
   int sum[10005] = {0},a[10005],b[10005],tmp,extra,i,j,start,length1,length2;
   char goal[10005];
   reverse(s.begin(),s.end());
   reverse(t.begin(),t.end());
   length1 = s.length();
   length2 = t.length();
   for(i = 0;i < length1;i++){
        a[i] = (int)(s[i] - '0');
   }
   for(i = 0;i < length2;i++){
        b[i] = (int)(t[i] - '0');
   }
   for(i = 0;i < length1;i++){
        start = i;
        for(j = 0;j < length2;j++){
            sum[start] += a[i]*b[j];
            start ++;
        }
   }
   for(i = 0;i < start;i++){
        sum[i + 1] += sum[i] / 10;
        sum[i] = sum[i] % 10;
   }
    while(sum[i] == 0){
        i --;
    }
    start = 0;
   for(j = i ;j >= 0;j--){
        goal[start] = (char)(sum[j] + '0');
        start ++;
   }
   goal[start] = '\0';
   return (string)goal;
}
 
int main(){
    string s,t;
    while(cin>>s>>t){
		if( s == "0" or t == "0" ){
			cout << "0" << endl;
			continue;
		}
		int a = 1;
		if( s[0] == '-' ){ a *= -1; s = s.substr(1,1000); }
		if( t[0] == '-' ){ a *= -1; t = t.substr(1,1000); }
        //cout<<s<<" "<<t<<endl;
        string ans = BigMul(s,t);
		if( a == -1 ) ans = '-' + ans;
		cout << ans << endl;
    }
}
 