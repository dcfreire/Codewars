void remove_leading(std::string& str) {
  while (str[str.length() - 1] == ' ') str.erase(str.length() - 1, 1);
}

std::string decodeMorse(std::string morseCode) {
  // ToDo: Accept dots, dashes and spaces, return human-readable message
  std::string decoded = "", dd = "";

  while (morseCode.length() != 0) {
    while (morseCode[0] != ' ' && morseCode.length() != 0) {
      dd += morseCode[0];
      morseCode.erase(0, 1);
    }

    if (morseCode.length() != 0) {
      morseCode.erase(0, 1);

      if (morseCode[0] == ' ') {
        morseCode.erase(0, 2);

        if (dd.length() > 0) decoded += MORSE_CODE[dd] + " ";
      } else {
        decoded += MORSE_CODE[dd];
      }
    } else {
      decoded += MORSE_CODE[dd];
    }
    dd.clear();
  }
  remove_leading(decoded);
  return decoded;
}
