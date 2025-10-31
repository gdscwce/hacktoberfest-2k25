#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
    sort(products.begin(), products.end());
    vector<vector<string>> res;
    string prefix;
    for(char c:searchWord){
        prefix+=c;
        vector<string> temp;
        for(string& p:products){
            if(p.substr(0,prefix.size())==prefix){
                temp.push_back(p);
                if(temp.size()==3) break;
            }
        }
        res.push_back(temp);
    }
    return res;
}

int main(){
    vector<string> products={"mobile","mouse","moneypot","monitor","mousepad"};
    string searchWord="mouse";
    vector<vector<string>> ans=suggestedProducts(products,searchWord);
    for(auto& v:ans){
        for(auto& s:v) cout<<s<<" ";
        cout<<endl;
    }
}
