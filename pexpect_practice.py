"""
1. input arg:  node_name
2. read commands from node_name.txt
3. lookup the console IP and tcp port for node_name
4. login into the node
5. send configuration commands
6. show commands
7. testing commands fro vpcs
8. capture results
"""
import pexpect
from gns3_node_search import fetch_node_console

project_name = "workshop_companion_5_nodes-1-int21"
node_name = 'dcb-38'
test_name = 'base'
gns3_ip = '192.168.135.134'


cli_file = "/Users/yzeng/Documents/Gates/My Documents/Working In Progress/Extreme/GNS3/GNS3/scripts/"+ node_name \
               + "_" + test_name + ".txt"

print ('cli_file is', cli_file)


child = pexpect.spawn('telnet {0} {1}'.format(gns3_ip, fetch_node_console(gns3_ip, project_name, node_name)))
child.sendline('')

child.expect('Login: ')

child.sendline('rwa')

child.expect('Password: ')

child.sendline('rwa')
child.sendline('enable')
child.sendline('conf term')


for line in open(cli_file):
    cmd = line.rstrip('\n')
    print (cmd)
    child.sendline(cmd)

child.sendline('save config')
child.sendline('exit')
child.close()


