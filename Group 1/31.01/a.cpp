#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int x, y, z;
    cin >> x >> y >> z;
    float s;
    if(x > z + y){
        s = exp(z / y);
    }else if(x < z + y){
        s = exp(y / z);
    }else{
        s = sin(z + y);
    }
    cout << s;
    return 0;
}