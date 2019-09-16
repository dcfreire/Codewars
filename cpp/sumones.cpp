#include <math.h>

long long countOnes ( int left, int right )
{
  double lower = log2(left) + 1;
  double upper = log2(right) + 1;
  double fu = floor(upper);
  double cl = ceil(lower);
  long long int ones = 0;

  while(fu >= cl){
    ones += pow(2, fu - 1) + pow(2, 2*fu - 5) + pow(2, fu - 3);
    fu--;
  }
  if(floor(lower) != lower){

  }
  if(ceil(upper) != upper){
    
  }
	return ones;
}