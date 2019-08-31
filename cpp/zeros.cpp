
#include <math.h>

long zeros(long n) {
  int ret = 0;

  for (int i = 1; i <= (int)(log(n) / log(5)); i++) ret += (int)(n / pow(5, i));

  return ret;
}