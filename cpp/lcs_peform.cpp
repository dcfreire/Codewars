#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <map>
using namespace std;

void update_table(vector<vector<int> >& tab, string x, string y) {
  int m = x.length();
  int n = y.length();

  for (int i = 1; i < m; i++) {
    for (int j = 1; j < n; j++) {
      if (x[i] == y[j]) tab[i][j] = tab[i - 1][j - 1] + 1;
      else
      if (tab[i - 1][j] >= tab[i][j - 1]) tab[i][j] = tab[i - 1][j];
      else tab[i][j] = tab[i][j - 1];
    }
  }
}

string lcs(const string& x, const string& y) {
  int c = y.length() - 1, up, left, here;

  cout << "x: " << x << endl;
  cout << "y: " << y << endl;

  string ret = "";
  vector<vector<int> > mat(x.length() + 1, vector<int>(y.length() + 1, 0));

  if (!x.length() || !y.length()) return "";


  update_table(mat, x, y);

  for (int i = 0; i < x.length(); i++) {
    for (int j = 0; j < y.length(); j++) {
      cout << " " << mat[i][j];
    }
    cout << endl;
  }

  for (int i = x.length() - 1; i >= 0; i--) {
    for (int j = c; j >= 0; j--) {
      here = mat[i][j];

      if (!here) {
        return ret;
      }

      if (j - 1 >= 0) {
        left = mat[i][j - 1];

        if (left == here) {
          cout << "gone left" << endl;

          c--;
          i++;
          break;
        }
      }

      if (i - 1 >= 0) {
        up = mat[i - 1][j];

        if (up == here) {
          cout << "gone up" << endl;
          break;
        }
      }

      ret.insert(ret.begin(), x[i]);
      cout << "Found at: " << i << " : " << ret << endl;
      c--;
      break;
    }
  }
  return ret;
}
