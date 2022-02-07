#include <bits\stdc++.h>
using namespace std;
int main(){
    int n; cin >> n;
    map<string, int> m;
    for(int i = 0 ;i < n; ++i){
        string name;
        cin >> name;
        m[name] = false;
    }

    cin >> n;
    for(int i = 0 ;i < n; ++i){
        string name;
        cin >> name;
        m[name] = true;
    }
}