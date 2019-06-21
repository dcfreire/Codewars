#include <math.h>
#include <map>


using ull = unsigned long long;
std::map<long int, ull> mem;

ull exp_sum(long int n) {
  ull sum    = 0;
  ull aux    = 1;
  long int k = 1;

  if (n == 0) return 1;

  if (n < 0) return 0;

  if (mem.count(n)) return mem[n];

  while (aux) {
    aux  = exp_sum(n - (k * (3 * k - 1) / 2));
    sum += pow(-1, k + 1) * aux;

    if (k > 0) k = k * (-1);
    else k = (k * (-1)) + 1;
  }
  mem[n] = sum;
  return sum;
}
