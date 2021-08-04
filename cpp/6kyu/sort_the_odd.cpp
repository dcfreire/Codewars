#include <stdlib.h>
#include <stdio.h>
#include <vector>

class Kata {
public:

  std::vector<int>sortArray(std::vector<int>array)
  {
    int aux;

    for (int i = 0; i < array.size(); i++) {
      for (int j = i + 1; j < array.size(); j++) {
        if (array[i] % 2 && array[j] % 2 && (array[i] > array[j])) {
          aux      = array[i];
          array[i] = array[j];
          array[j] = aux;
        }
      }
    }
    return array;
  }
};
