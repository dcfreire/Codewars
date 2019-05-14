#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

void update_table(vector<vector<int> > &tab, int x, int y){
        for(int i = x; i < tab.size(); i++)
                for(int j = y; j < tab[0].size(); j++)
                        tab[i][j]++;

}

string lcs(const string& x, const string& y){
        int n = 1, c =0;
        cout << "x: " << x << endl;
        cout << "y: " << y<<endl;

        string ret = "";
        vector<vector<int> > mat(x.length()+1, vector<int>(y.length()+1, 0));
        for(int i = 0; i < x.length(); i++) {
                for(int j = 0; j < y.length(); j++) {
                        if(x[i] == y[j])
                                update_table(mat, i, j);
                }
        }
        for(int i = 0; i <= x.length(); i++) {
                for(int j = 0; j <= y.length(); j++) {
                        cout << " " <<mat[i][j];
                }
                cout << endl;
        }
        for(int i = 0; i < x.length(); i++) {
                for(int j = c; j < y.length(); j++) {
                        if(mat[i][j] == n) {
                                ret += x[i];
                                c++;
                                n++;
                                break;
                        }else{
                                if(mat[i][j+1] == n) {
                                        ret = x[i];
                                        c+=2;
                                        n++;
                                        break;
                                }else{
                                        if(mat[i+1][j] == n) {
                                                ret += y[j];
                                                i++;
                                                c++;
                                                n++;
                                                break;
                                        }else{
                                                
                                                break;
                                        }
                                }

                        }
                }
        }
        return ret;
}
