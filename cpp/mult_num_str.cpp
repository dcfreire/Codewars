#include <iostream>
#include <string>
#include <vector>
using namespace std;

void remove_zeros(string &a){
  string::iterator it = a.begin();
  if(it == (a.end()-1))
    return;
  if(*it == '0'){
    a.erase(it);
    remove_zeros(a);
  }
  return;
}

string multiply(string a, string b) {
  remove_zeros(a);
  remove_zeros(b);
  cout <<"A: " <<a << endl;
  cout <<"B: " <<b << endl;
  if(a.length() >= b.length())
    swap(a, b);

  int alen = a.length();
  string ret1;
  vector<string> ret(alen);
  int u, t, resto = 0, restoant = 0;
  for(int i = alen-1; i >= 0; i --){
    for(int j = alen - 1 - i; j > 0; j--)
      ret[i].append("0");
  }
  int c = alen-1;

  for(string::iterator itA = a.end()-1; itA >= a.begin(); itA--){
    for(string::iterator itB = b.end()-1; itB >= b.begin(); itB--){
      u = (*itA - '0')*(*itB - '0') +  resto;
      resto = 0;
      if(u > 9){
        resto = u/10;
        u = u%10;
      }
      ret[c].insert(0, to_string(u));
    }
    if(resto)
      ret[c].insert(0, to_string(resto));
    c--;
    resto = 0;
  }
  for(int i = alen-1; i >= 0; i --){
      cout<< ret[i] << "+" << endl;
  }
  resto = 0;
  restoant = 0;
  string::iterator is;
  string last = ret.back();
  char lastchar = last.back();
  ret1.push_back(lastchar);

    for(int col = 1; col < ret[0].length(); col++){
      for(vector<string>::iterator in = ret.end()-1; in >= ret.begin(); in--){
        if(col < in->length()){
          is = in->end() - col-1;
          t += (*is - '0') + restoant;
          if(t > 9){
            resto += t/10;
            t = t % 10;
          }
          restoant = 0;
        }
    }
          restoant = resto;
          resto = 0;
          ret1.insert(0, to_string(t));
          t = 0;

    }
    if(restoant)
      ret1.insert(0, to_string(restoant));
    remove_zeros(ret1);
    if(ret1.length() == 0)
      return "0";
  return ret1;
}
