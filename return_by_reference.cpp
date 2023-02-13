#include<iostream>
using namespace std;
int & swapnumber(int &a,int &b){
    int t=a;
    a=b;
    b=t;
    return a;
}

int main(){
    int x=9,y=8;
    swapnumber(x,y)=766;
    cout<<"value of x="<<x<<"value of y="<<y<<endl;
    
    return 0;
}