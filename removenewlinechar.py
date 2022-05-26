#!/usr/bin/python3
import sys

print('## input Text ##')
input = sys.stdin.readlines()
s = ''
for i in input:
    s += i
string = s.split() #나중에 .\n으로 끊으면 완벽
for i,word in enumerate(string):
    if word[-1] == '.':
        string[i] += '\n'

modified_string = ' '.join(string)
modified_string = modified_string.replace('.\n ','.\n')
#modified_string.replace('.\n ','.\n')
print('\n### modified_string ###')
print(modified_string)
