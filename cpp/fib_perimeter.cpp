typedef unsigned long long ull;
class SumFct {
public:

  static ull perimeter(int n) {
    ull sum = 0;
    ull aux = 1, aux2 = 1, aux3;

    for (int i = 0; i <= n; i++) {
      if (i < 2) {
        sum += aux;
        continue;
      }
      aux3 = aux2;
      aux2 = aux + aux2;
      aux  = aux3;
      sum += aux2;
    }
    sum *= 4;
    return sum;
  }
};
