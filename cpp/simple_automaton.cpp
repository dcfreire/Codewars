#include <regex>
class Automaton
{
public:
  Automaton():fsmregex("^0*1(1|0(1|0))*$") {}
  bool read_commands(const std::vector<char>& commands){
    std::string s(commands.begin(), commands.end());
    return std::regex_match(s, fsmregex);
  }
private:
  std::regex fsmregex;
};
