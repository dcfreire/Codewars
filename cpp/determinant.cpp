#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

long long determinant(vector< vector<long long> > m) {
  if(m.size() == 0)
    return 0;
  if(m.size() == 1)
    return m[0][0];
  if(m.size() == 2)
    return (m[0][0] * m[1][1]) - (m[1][0] * m[0][1]);
  else{
    vector< vector< long long> > minor;
    long long det = 0;
    for(int i = 0; i < m.size(); i++){
      auto aux = m;
      for(int j = 1; j < m.size(); j++){
        aux[j].erase(aux[j].begin() + i);
        minor.push_back(aux[j]);
      }
      det += (m[0][i] * determinant(minor) * pow(-1, i));
      minor.clear();
    }
    return det;
  }
}
