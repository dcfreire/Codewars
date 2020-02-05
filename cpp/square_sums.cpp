#include <vector>
#include <map>
#include <math.h>
#include <fstream>
#include <algorithm>
//std::vector<std::vector<bool>> graph(1001, std::vector<bool>(1001, 0));
std::map<int, std::vector<int>> graph;
std::vector<int> sol;
void run_once(){
  for(int i = 1; i < 1000; i++){
    for(int f = i+1; f < 1000; f++){
        double a = sqrt(i+f);
        if(a == (int)a){
          graph[i].push_back(f);
          graph[f].push_back(i);
      }
    }
  }
}

std::vector<int> find_next(std::vector<int> trace, int pos, int n){
  int j = graph[pos][0];
  std::vector<int> ret;
  int c = 0;
  while(j <= n){
    if(!std::count(trace.begin(), trace.end(), j))
      ret.push_back(j);
    c++;
    j = graph[pos][c];
  }
  return ret;
}

void square_aux(int n, int cur, std::vector<int> trace){
  std::vector<int> next;
  trace.push_back(cur);
  next = find_next(trace, cur, n);
  if(!sol.empty())
    return;
  if(trace.size() == n){ 
    sol = trace;
    return;
    }

  if(next.size()){
    for(int i = 0; i < next.size(); i++){
      square_aux(n, next[i], trace);
    }
}
}


std::vector<int> square_sums_row(int n){
  if(graph.empty()){
    run_once();
  }
  int start = sqrt(n);
  start *= start;
  for(int i = 1; i <= n; i++){
    square_aux(n, i, std::vector<int>());
    if(!sol.empty)
      break;
  }
  std::vector<int> ret = sol;
  sol.clear();
  return ret;
}

int main(){
  auto x = square_sums_row(23);
  std::ofstream of;
  of.open("out.dot");
  of << "graph G {" << std::endl;
  for(int i = 1; i < 16; i++){
    int j = graph[i][0];
    int c = 0;
    while(j < 16){
        of << " " << i << " -- " << j << ";" <<std::endl;
        c++;
        j = graph[i][c];
    }
  }
  of << "}";
}