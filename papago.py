#!/usr/bin/python3
import sys
import os
import sys
import urllib.request, json


def inputText():
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
    #print('\n###=======================###')
    #print(modified_string)
    return modified_string


client_id = "*********************" # 개발자센터에서 발급받은 Client ID 값
client_secret = "**********" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote(inputText()) # 번역할 값 입력
data = "source=en&target=ko&text=" + encText #source=번역할 언어, target=번역된 언어
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    #print(response_body.decode('utf-8'))
    print('## Translated Text ##')
    print(json.loads(response_body.decode('utf-8'))['message']['result']['translatedText'])
else:
    print("Error Code:" + rescode)



