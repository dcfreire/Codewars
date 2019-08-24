template <int m, int n>
struct ackermann {
 enum {value = ackermann<m - 1, ackermann<m, n - 1>::value>::value};

};

template <int m>
struct ackermann<m ,0> {
 enum {value = ackermann<m - 1, 1>::value};
 };

template <int n>
struct ackermann<0, n> {
 enum {value = n + 1};
 };
