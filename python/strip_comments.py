import re
def solution(string,markers):
    return re.sub(r"(\s*[" + ''.join(markers) +"].*)", "", string)