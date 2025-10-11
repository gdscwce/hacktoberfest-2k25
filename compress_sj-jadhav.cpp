#include <iostream>
#include <vector>
#include <string>
using namespace std;

int compress(vector<char>& chars){
    intn=chars.size();
    int write=0;
    for(int read=0;read<n;){
        char curr=chars[read];
        int count=0;
        while(read<n&&chars[read]==curr){
            ++read;
            ++count;
        }
        chars[write++]=curr;
        if(count>1){
            string cnt=to_string(count);
            for(char d:cnt)chars[write++]=d;
        }
    }
    return write;
}

int main(){
    string s;
    if(!(cin>>s))return 0;
    vector<char> chars(s.begin(),s.end());
    int newLen=compress(chars);
    cout<<newLen<<endl;
    for(int i=0;i<newLen;++i)cout<<chars[i];
    cout<<endl;
    return 0;
}
