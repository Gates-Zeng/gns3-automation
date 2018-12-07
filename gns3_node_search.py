"""
searches the project and node-name
returns the console tcp port numbers
"""

import requests


def fetch_node_console(gns3_ip, project_name, node_name):

    project_base_url = 'http://' + gns3_ip + ':3080/v2/projects'
    resp = requests.get(project_base_url)
    data = resp.json()

    # pprint(data)
    # pprint(data[0]['capabilities']['node_types'][3][1][2])
    # for k,v in data[0].items():
    #     print(k,v)
    # project = 'TBD'

    project_id = None

    for i in data:
        for k,v in i.items():
            if k == 'name' and v== project_name:
                project_id = i['project_id']
                print(project_id)


    if project_id != None:
        print(project_name, project_id)

    project_url = project_base_url + '/' + project_id + '/nodes'
    print ('project_url', project_url)
    resp_node = requests.get(project_url)
    data_node = resp_node.json()

    # pprint(data_node)
    # pprint(data[0]['capabilities']['node_types'][3][1][2])
    # for k,v in data[0].items():
    #     print(k,v)
    # project = 'TBD'

    console_port = None

    for i in data_node:
        for k,v in i.items():
            if k == 'name' and v == node_name:
                console_port = i['console']
                print(console_port)


    if console_port != None:
        print(node_name, console_port)
        return (console_port)
    else:
        pass


if __name__ == '__main_':
    print('console_port is', fetch_node_console ('192.168.135.134', project_name, node_name))

