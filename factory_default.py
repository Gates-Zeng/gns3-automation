from push_config import default_sw

#project_name = "workshop_companion_5_nodes-1-int40"
project_name = "fabric-ws-5-nodes-int040-1"

gns3_ip = '192.168.135.127'


node_list = [
     'DCA-30',
    'Core-34',
    'DCB-38',
    'CMPa-50',
    'CMPb-54'
]


i = 0

while i < len(node_list):
    print(node_list[i])
    default_sw(gns3_ip, project_name, node_list[i], 'voss')
    i += 1

"""
Because FA is not supported
Taking all EXOS switch out of the tests
"""


node_list = [
    'DCAEdge',
    'DCBEdge',
    'CMPaEdg',
    'CMPbEdg'
]


'''
i = 0

while i < len(node_list):
    print(node_list[i])
    default_sw(gns3_ip, project_name, node_list[i], 'exos')
    i += 1

'''

