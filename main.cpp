#include<bits/stdc++.h>
#include"core/clientdll.hpp"
#include"core/serverdll.hpp"
#include"core/clientpl.hpp"
#include"core/serverpl.hpp"
#include"helper/StrToBits.hpp"

using namespace std;

int main(){
    string s;
    cout << "Enter the message : ";
    getline(cin,s);
    
    string bits = StrToBits(s);
    
    return 0;
}