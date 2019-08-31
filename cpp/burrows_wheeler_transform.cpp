#include <utility>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

std::vector<std::string> transform(const std::string& s){
    std::vector<std::string> ret;
    for(int i = 0; i < s.length(); i++){
        std::string aux = s;
        aux.insert(0, aux, s.length()-i, i).erase(aux.end() - i, aux.end());
        ret.push_back(aux);
    }
    return ret;
}


std::pair<std::string, int> encode(const std::string& s) {
    std::vector<std::string> trans = transform(s);
    std::string ret;
    std::sort(trans.begin(), trans.end());
    ptrdiff_t pos = std::distance(trans.begin(), std::find(trans.begin(), trans.end(), s));
    for(auto t: trans){
        ret.push_back(t.back());
    }
    return {ret, pos};
}

std::string decode(const std::string& s, int n) {
    if(s.length() <= 1 || n > s.length() || n < 0)
        return s;
    std::vector<std::string> clist;
    for(int i = 0; i < s.length(); i++){
        clist.push_back(std::string(1, s[i]));
        
    }
    auto aux = clist;

    while(clist[0].length() < s.length()){
        std::sort(clist.begin(), clist.end());
        for(int i = 0; i < clist.size(); i++){
            clist[i].insert(0, aux[i]);
        }
    }
    std::sort(clist.begin(), clist.end());
    return clist[n];
}