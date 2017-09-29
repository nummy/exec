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

int changeToNumber(char c) { //change the char to integer
  if (c >= '0' && c <= '9')
    return c - '0';
  if (c >= 'a' && c <= 'z') {
    return c - 'a' + 10;
  }
  return -1;
}

bool checkIllegal(string num, long base) {// check the num is illegal
  for (int i = 0; i < num.size(); i++) {
    int number = changeToNumber(num[i]);
    if (number >= base || number == -1) {
      return false;
    }
  }
  return true;
}

bool metadrome(string num, long base) {
  if (!checkIllegal(num, base))
    return false;
  for (int i = 1; i < num.size(); i++) {
    if (changeToNumber(num[i]) <= changeToNumber(num[i - 1])) //if num[i] <= num[i-1],then it must not be metadrome
      return false;
  }
  return true;
}

bool plaindrome(string num, long base) {
  if (!checkIllegal(num, base))
    return false;
  for (int i = 1; i < num.size(); i++) {
    if (changeToNumber(num[i]) < changeToNumber(num[i - 1]))
      return false;
  }
  return true;
}

bool katadrome(string num, long base) {
  if (!checkIllegal(num, base))
    return false;
  for (int i = 1; i < num.size(); i++) {
    if (changeToNumber(num[i]) >= changeToNumber(num[i - 1]))
      return false;
  }
  return true;
}

bool nialpdrome(string num, long base) {
  if (!checkIllegal(num, base))
    return false;
  for (int i = 1; i < num.size(); i++) {
    if (changeToNumber(num[i]) > changeToNumber(num[i - 1]))
      return false;
  }
  return true;
}


string classify(string num, long base) {
  if (!checkIllegal(num, base)) { // if illeag return nondrome
    return "nondrome";
  }
  if (metadrome(num, base)) {
    return "metadrome";
  }
  if (plaindrome(num, base)) {
    return "plaindrome";
  }
  if (katadrome(num, base)) {
    return "katadrome";
  }
  if (nialpdrome(num, base)) {
    return "nialpdrome";
  }
  return "nondrome"; //not match any return nondrome
}

int main() {
  string num;
  long base;
  cout << boolalpha;
  cin >> num >> base;
  cout << metadrome(num, base) << " "
       << plaindrome(num, base) << " "
       << katadrome(num, base) << " "
       << nialpdrome(num, base) << " "
       << classify(num, base) << endl;
}
