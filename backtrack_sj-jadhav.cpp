#include <iostream>
#include <vector>
#include <string>
using namespace std;

void backtrack(string digits,string path,int index,vector<string>& res,vector<string>& map){
    if(index==digits.size()){
        res.push_back(path);
        return;
    }
    string letters=map[digits[index]-'0'];
    for(char c:letters) backtrack(digits,path+c,index+1,res,map);
}

vector<string> letterCombinations(string digits){
    if(digits.empty()) return {};
    vector<string> map={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    vector<string> res;
    backtrack(digits,"",0,res,map);
    return res;
}

int main(){
    string digits="23";
    vector<string> ans=letterCombinations(digits);
    for(string s:ans) cout<<s<<" ";
}
