import requests
from pprint import pprint

resp = requests.get('http://192.168.135.128:3080/v2/projects')
data = resp.json()

pprint(data)
# pprint(data[0]['capabilities']['node_types'][3][1][2])
# for k,v in data[0].items():
#     print(k,v)
project = 'api_created'
# project = 'TBD'

project_id = None

for i in data:
    for k,v in i.items():
        if k == 'name' and v== project:
            project_id = i['project_id']
            print(project_id)


if project_id != None:
    print(project, project_id)
else:
    post_data = '{"name": "' + project + '"}'
    resp = requests.post('http://192.168.135.128:3080/v2/projects', data=post_data)
    project_id = resp.json()['project_id']
    print(resp.status_code, resp.reason)
    print(project_id)


