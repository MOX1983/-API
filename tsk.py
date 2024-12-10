import requests
import csv
import os
from dotenv import load_dotenv
load_dotenv()



def posts():
    tocen = os.getenv('tocen')
    v = os.getenv('v')
    domen = os.getenv('domen')
    count = 100
    offset = 0
    all_post = list()

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': tocen,
                                    'v': v,
                                    'domain': domen,
                                    'count': count,
                                    'offset': offset
                                })

        data = response.json()['response']['items']
        offset += 100
        all_post.extend(data)
    return all_post

def write_fail(data):
    with open('kuplinovplay.csv', 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(['like', 'body', 'url'])
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img = post['attachments'][0]['link']['photo']['sizes'][-1]['url']
                else:
                    img= 'none'
            except:
                pass

            writer.writerow((post['likes']['count'], post['text'], img))


all_post = posts()
write_fail(all_post)

print(1)