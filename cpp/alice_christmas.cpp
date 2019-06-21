#include <vector>
#include <algorithm>
int largest_visible_area(int k, std::vector<std::pair<int, int> >cylinders) {
  std::vector<int> r, m, total;
  int aux, area;

  for (std::vector<std::pair<int, int> >::iterator it = cylinders.begin();
       it != cylinders.end(); it++) {
    r.push_back(it->first);
    m.push_back(it->second);
  }

  for (int i = 0; i < cylinders.size(); i++) {
    for (int j = i + 1; j < cylinders.size(); j++) {
      if (r[i] > r[j]) {
        aux  = r[i];
        r[i] = r[j];
        r[j] = aux;
        aux  = m[i];
        m[i] = m[j];
        m[j] = aux;
      }
    }
  }
  r.push_back(-1);

  for (int i = 0; i < cylinders.size(); i++) {
    total.push_back(r[i] + m[i]);

    if (r[i] == r[i + 1])
      if (m[i] < m[i + 1]) {
        r.erase(r.begin() + i);
        m.erase(m.begin() + i);
        total.erase(total.begin() + i);
      }
  }

  for (int i = 0; i < total.size(); i++) {
    for (int j = i + 1; j < total.size(); j++) {
      if (total[i] < total[j]) {
        aux      = total[i];
        total[i] = total[j];
        total[j] = aux;
        aux      = r[i];
        r[i]     = r[j];
        r[j]     = aux;
        aux      = m[i];
        m[i]     = m[j];
        m[j]     = aux;
      }
    }
  }
  for(int i = 0; i < k; i++)
    area += total[i] - r[i];
  return area;
}

int main() {}
