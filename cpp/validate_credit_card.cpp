

class Kata {
  public:
  static bool validate(long long int n) {
    long long int aux = n;
    int digit;
    int sum = 0;
    int par = 4;
    while(aux > 0){
      digit = aux % 10;
      if(par % 2){
        digit *= 2;
        if(digit > 9)
          digit -= 9;
      }
      par++;
      sum += digit;
      aux /= 10;
    }
    return 0 == (sum % 10);
  }
};
