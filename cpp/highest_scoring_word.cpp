#include <string>
#include <iostream>
#include <stdlib.h>
using namespace std;

std::string highestScoringWord(const std::string &str){
  std::string best_word;
  int score = 0;
  int c = 0, aux;
  int bestscore = 0;
  for(int i = 0; i < str.length(); i++){
    aux = i;
    while((int)str[i] > 96){
      score+= (int)str[i]-96;
      i++;
      c++;

    }
    if(score > bestscore){
      best_word = str.substr(aux, c);
      bestscore = score;
    }
    score = 0;
    c = 0;
  }
  return best_word;
}
