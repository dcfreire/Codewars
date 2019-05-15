class Machine {
public:
    Machine(): last(2) {}
    unsigned int command(unsigned int cmd, unsigned int num){
      if(this->res[cmd] != 0)
        return get_action(res[cmd] - 1)(num);
      unsigned int r = rand() % 5;
      this->last[0] = cmd;
      this->last[1] = r;
      unsigned int ret = get_action(r)(num);
      return ret;
    }
    void response(bool res){
      if(res)
        this->res[this->last[0]] = this->last[1] + 1;
      else
        this->res[this->last[0]] = 0;
    }
private:
  std::vector<unsigned int> last;
  std::map<unsigned int,unsigned int> res;
};
