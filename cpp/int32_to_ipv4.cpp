#include<stdlib.h>
#include<string>
#include<iostream>
std::string uint32_to_ip(uint32_t ip)
{
  int octet = 3;
  std::string ret;
  while(octet >= 0){
    ret.append((std::to_string((ip >> (8*octet)) & 0b11111111)));
    if(octet)
      ret.append(".");
    octet--;
  }
  return ret;
}

int main(){
  std::cout << uint32_to_ip(2149583361);
}
