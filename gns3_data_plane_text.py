from push_config import push_config, push_test, capture_test


project_name = "fabric-ws-5-nodes-int040-1"

# gns3_ip = '192.168.10.210'

# project_name = "workshop_companion_5_nodes-1-int40-1"


gns3_ip = '192.168.135.134'


node_list_voss = [
    'DCA-30',
    'Core-34',
    'DCB-38',
    'CMPa-50',
    'CMPb-54'
]


node_list_exos = [
    'DCAEdge',
    'DCBEdge',
    'CMPaEdg',
    'CMPbEdg'
]


''' The PC name will be used to map to:
 1. CLI file (for example PCDCA.txt
 2. Test case from vm file csv
 3. Determine the IP address and ping across fabric
 '''

node_list_pc = [
    'PCDCA',
    'PCDCB',
    'PCCMPa',
    'PCCMPb'
]

test_list = [
#       ('mgmt', '0'),
#       ('base', '0'),
       ('l2vsn-240', '3'),
#       ('l2vsn-trans', '4'),
#       ('l2vsn-inter', '5'),
#       ('ipsc', '0'),
#       ('l3vsn', '1'),
#       ('l3vsn-2', '2'),
#       ('l2_l3vsn', '5'),
#     ('fe', '5')
]


for k, v in test_list:

    config_name = k

    i = 0

    while i < len(node_list_voss):
        print(node_list_voss[i])
        push_config(gns3_ip, project_name, node_list_voss[i], 'voss', config_name)
        i += 1

    '''
    i = 0

    while i < len(node_list_exos):
        print(node_list_exos[i])
        push_config(gns3_ip, project_name, node_list_exos[i], 'exos', config_name)
        i += 1

    '''

    i = 0

    while i < len(node_list_pc) and v != '0':
        print(node_list_pc[i])
        push_test(gns3_ip, project_name, node_list_pc[i], 'vpc', test_group=v)
        i += 1

    i = 0

    while i < len(node_list_voss):
        print(node_list_voss[i])
        capture_test (gns3_ip, project_name, node_list_voss[i], 'voss', config_name)
        i += 1

