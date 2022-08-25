#include <iostream>
#include <string>
#include <vector>


using namespace std;
bool is_duplicate(vector<string>s, string in) {
  for (int i = 0; i < s.size(); i++) {
    if (!in.compare(s[i])) return true;
  }
  return false;
}

void permutate(vector<string> *s, string str, int nfixed, int dir) {
  if (dir != 1)
    if (!is_duplicate(*s, str)) s->push_back(str);

  if (nfixed == str.length() - 1) return;

  for (int i = str.length() - 1; i > nfixed; i--) {
    permutate(s, str, nfixed + 1, 1);

    if (nfixed != i) {
      std::swap(str[i], str[nfixed]);
      permutate(s, str, nfixed + 1, -1);
    }
  }
}

vector<string>permutations(string s) {
  vector<string> ret;

  ret.push_back(s);
  permutate(&ret, s, 0, 0);
  return ret;
}
