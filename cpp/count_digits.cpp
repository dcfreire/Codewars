#include <stdlib.h>
#include <stdio.h>
#include <vector>

class CountDig {
public:

  static int nbDig(int n, int d) {
    int square;
    int dcount = 0;

    for (int i = 0; i <= n; i++) {
      square = i * i;

      do {
        if (square % 10 == d) dcount++;

        square /= 10;
      } while (square > 0);
    }
    return dcount;
  }
};
