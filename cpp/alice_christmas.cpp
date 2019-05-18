#include <vector>

int largest_visible_area(int k, std::vector<std::pair<int, int>> cylinders) {
  std::vector<int> r, m;
  int aux, area;
  for(std::vector<std::pair<int, int>>::iterator it = cylinders.begin(); it != cylinders.end(); it++){
    r.push_back(it->first);
    m.push_back(it->second);
  }
  for(int i = 0; i < cylinders.size(); i++){
    for(int j = i+1; j < cylinders.size(); j++){
      if(m[i] < m[j]){
        aux = r[i];
        r[i] = r[j];
        r[j] = aux;
        aux = m[i];
        m[i] = m[j];
        m[j] = aux;
      }
    }
  }
  r.push_back(-1);
  for(int i = 0; i < cylinders.size(); i++){
    if(r[i] != r[i+1]){
      area += r[i]*r[i] + m[i];
  }else{
    if(m[i] > m[i+1]){
      m.erase(m.begin() + i+1);
      r.erase(r.begin() + i+1);
      i--;
    }else{
      m.erase(m.begin() + i);
      r.erase(r.begin() + i);
      i--;
    }
  }
}
  return area;
}

int main(){
}
