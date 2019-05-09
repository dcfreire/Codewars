#include <vector>
#include <stdlib.h>

class Tortoise
{
public:
    static std::vector<int> race(int v1, int v2, int g){
      double exact_time = ((double)g/((double)(v2-v1)))*(double)(60*60);
      double md, sd;
      int h, m, s;
      if(exact_time < 0)
        return {-1,-1,-1};
      h = (int)exact_time/(60*60);
      md = (exact_time/60 - h*60);
      m = md;
      sd = (md - m)*60;
      s = (exact_time - m*60 - h*(60*60));


      return {(int)h, (int)m, (int)s};
    }
};
