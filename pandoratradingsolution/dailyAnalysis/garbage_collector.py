import os
import requests
import json

url = 'http://127.0.0.1:8000/dailyanalysis/api/posts/?format=json'
responce = requests.get(url)

print('POST UUIDs:')
uuid_list = []
for p in json.loads(responce.text)['posts']:
    print(p['slug'])
    uuid_list.append(p['slug'])

cd = os.path.abspath(os.curdir)
print(cd)
print(os.path.split(cd))
media_path = os.path.split(cd)[0] + r'/media/dailyAnalysis'
print(media_path)
print(os.listdir(media_path))

print('IMAGEs:')
for i in os.listdir(media_path):
    file_uuid = i.split('_')[-1].split('.')[0]
    print(file_uuid)
    if file_uuid not in uuid_list:
        print('DELETE: ' + i)
        os.remove(media_path + r'/' + i)
