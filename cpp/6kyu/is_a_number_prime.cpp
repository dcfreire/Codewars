bool isPrime(int num) {
  int i;

  if ((num == 2) || (num == 3)) return true;

  if ((num == 1) || (num <= 0) || (num % 2 == 0) || (num % 3 == 0)) {
    return false;
  }
  i = 5;

  while (i * i <= num) {
    if ((num % i == 0) || (num % (i + 2) == 0)) return false;

    i += 6;
  }
  return true;
}
