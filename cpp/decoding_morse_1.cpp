std::string decodeMorse(std::string morseCode) {
        // ToDo: Accept dots, dashes and spaces, return human-readable message
        std::string decoded, dd = "";
        while(morseCode.length() != 0) {
                while(morseCode[0] != ' ' && morseCode.length() != 0) {
                        dd += morseCode[0];
                        morseCode.erase(0, 1);
                }
                if(morseCode.length() != 0) {
                        if(morseCode[0] = ' ') {
                                morseCode.erase(0, 3);
                                decoded += MORSE_CODE[ dd ] + " ";
                        }else{
                                morseCode.erase(0, 1);
                                decoded += MORSE_CODE[ dd ];
                        }
                }else{
                        decoded += MORSE_CODE[ dd ];
                }
                dd.clear();
        }
        return decoded;
}
