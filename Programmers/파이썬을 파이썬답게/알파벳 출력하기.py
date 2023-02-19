'''
import string
string.ascii_lowercase : 알파벳 소문자 모두
string.ascii_uppercase : 알파벳 대문자 모두
string.ascii_letters : 알파벳 대소문자 모두
string.digits : 숫자 모두

string >> https://docs.python.org/3.4/library/string.html
'''

import string
num = int(input().strip())
# 내가 푼 풀이
for i in range(26):
    if num == 0:
        print(chr(i + ord('a')), end='')
    else:
        print(chr(i + ord('A')), end='')

# string을 쓰는 풀이
if num == 0:
    print(string.ascii_lowercase)
else:
    print(string.ascii_uppercase)

