class Suite {
public:

  static double going(int n) {
    double ret = 1, prev = 1, scale = 0.000001;

    for (int i = 0; i < n - 1; i++) {
      prev /= n - i;
      ret  += prev;
    }
    ret = (int)(ret / scale) * scale;
    return ret;
  }
};
