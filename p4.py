from push_config import default_sw, upgrade_sw, cleanup_sw

project_name = "workshop_companion_5_nodes-1-int40"

gns3_ip = '192.168.135.127'
# gns3_ip = '192.168.10.210'


node_list = [
    'DCA-30',
    'Core-34',
    'DCB-38',
    'CMPa-50',
    'CMPb-54'
]

'''
i = 0

while i < len(node_list):
    print(node_list[i])
    sw_ip = '192.168.255.' + node_list[i].split('-',1)[1]
    print('switch_ip:', sw_ip)
    upgrade_sw(gns3_ip, project_name, sw_ip, node_list[i], 'voss', 'VOSS1K.91.18.1.0int040.tgz')
    i += 1
'''

i = 0

while i < len(node_list):
    print(node_list[i])
    sw_ip = '192.168.255.' + node_list[i].split('-',1)[1]
    print('switch_ip:', sw_ip)
    cleanup_sw(gns3_ip, project_name, node_list[i], 'voss', 'VOSS1K.91.18.1.0int038')
    i += 1




