#include<iostream>
using namespace std;

int main(){
    int n,ans=0;
    string a;
    cin>>n;
    // n-=1;
    while(n--){
        cin>>a;
        if(a=="X++")ans++;
        else if(a=="++X")++ans;
        else if(a=="X--")ans--;
        else --ans;
    }
    // cin>>a;
    cout<<ans;
    return 0;
}