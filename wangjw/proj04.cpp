#include<iostream>
using std::cout; using std::cin; using std::endl; using std::boolalpha;
#include<string>
using std::string;
             
// meta, strictly increase
// plain, non-strictly increase
// kata, strictly decrease
// nialp, non-strictly decrease
// non, none of the above

const string base_vals = "0123456789abcdefghijklmnopqrstuvwxyz";


int main (){
  string num;
  long base;
  cout << boolalpha;
  cin >> num >> base;
  cout << metadrome (num, base) << " "
       << plaindrome (num, base) << " "
       << katadrome (num, base) << " "
       << nialpdrome (num, base) << " "
       << classify(num, base) << endl;
}
    



  
