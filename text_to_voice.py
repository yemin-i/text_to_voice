#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
import os

url = 'https://kakaoi-newtone-openapi.kakao.com/v1/synthesize'

# content type = xml, authorization 값
headers = {
    'Content-Type' : 'application/xml',
    'Authorization' : 'REST_API_KEY'
}

# 음성으로 들려 줄 데이터를 만들기
def make_data(text):
    data = '''
    <speak>
    <voice> %s </voice>
    </speak>
    ''' % text
    return data.encode('utf-8')  # 한글 출력을 위해 utf-8로 인코딩

while True:
    cmd = input('입력하세요 : ')
    # 종료 조건
    if cmd == 'end':
        print('종료되었습니다.')
        break
    # 입력된 단어를 음성으로 출력
    else:
        data=make_data(cmd)
        res = requests.post(url, data=data, headers=headers)  # post 요청

        with open('voice.mp3', 'wb') as f:
            f.write(res.content)   # content를 통해 binary 형식의 원문 쓰기
 
        os.system('start voice.mp3')   # 파일 호출


# In[ ]:




