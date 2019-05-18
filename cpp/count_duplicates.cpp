size_t duplicateCount(const std::string& in); // helper for tests
#include <string.h>

size_t duplicateCount(const char *in)
{
  int  c    = 0;
  bool done = false;
  int  len  = strlen(in);

  char a[len];

  for (int i = 0; i < strlen(in); i++) {
    a[i] = in[i];
  }

  for (int i = 0; i < strlen(in); i++) {
    for (int f = i + 1; f < strlen(in); f++) {
      if (a[i] == (char)NULL) break;

      if (((int)a[f] == (int)a[i]) || ((int)a[f] == (int)a[i] - 32) ||
          ((int)a[f] - 32 == (int)a[i])) {
        if (!done) c++;

        a[f] = (char)NULL;

        done = true;
      }
    }
    done = false;
  }

  return c;
}
