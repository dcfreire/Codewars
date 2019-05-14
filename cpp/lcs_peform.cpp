#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <map>
using namespace std;

void update_table(vector<vector<int> > &tab, int x, int y, char ch, string b){
        int a = tab[x][y];
        bool first = true;
        for(int i = x; i < tab.size(); i++)
                for(int j = y; j < tab[0].size(); j++){
                        if((tab[i][j]) < (a+1)){
                          if(b[j] != ch || first){
                            tab[i][j]++;
                            first = false;
                          }
                        }
                        first = true;
                      }

}

string lcs(const string& x, const string& y){
        int n = 0, c = y.length()-1, up, left, here;
        cout << "x: " << x << endl;
        cout << "y: " << y<<endl;

        string ret = "";
        vector<vector<int> > mat(x.length(), vector<int>(y.length(), 0));
        if(!x.length() || !y.length())
          return "";


        for(int i = 0; i < x.length(); i++) {
                for(int j = 0; j < y.length(); j++) {
                        if(x[i] == y[j]){
                          for(int i = 0; i < x.length(); i++) {
                                  for(int j = 0; j < y.length(); j++) {
                                          cout << " " <<mat[i][j];
                                  }
                                  cout << endl;
                          }
                          cout << endl;

                                update_table(mat, i, j, y[j], y);
                              }

                }
        }
        for(int i = 0; i < x.length(); i++) {
                for(int j = 0; j < y.length(); j++) {
                        cout << " " <<mat[i][j];
                }
                cout << endl;
        }
        for(int i = x.length()-1; i >= 0; i--) {
                for(int j = c; j >= 0; j--) {
                        here = mat[i][j];
                        if(!here){
                          return ret;
                        }
                        if(j-1 >= 0) {
                                left = mat[i][j-1];

                                if(left == here) {
                                  cout << "gone left" << endl;

                                        c--;
                                        i++;
                                        break;
                                }
                        }
                        if(i-1 >= 0) {
                                up = mat[i-1][j];
                                if(up == here) {
                                        cout << "gone up" << endl;
                                        break;
                                }
                        }

                        ret.insert(ret.begin(), x[i]);
                        cout << "Found at: " << i <<" : "<< ret << endl;
                        c--;
                        break;

                }
        }
        return ret;

}
