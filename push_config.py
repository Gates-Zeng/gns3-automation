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
from ping_test import ping_test


def push_config(gns3_ip, project_name, node_name, node_type, config_name):
    cli_file = "/Users/yzeng/Documents/Gates/My Documents/Working In Progress/Extreme/GNS3/GNS3/scripts/5-nodes/" \
               + config_name + '/' + node_name + ".txt"
    print('starting', node_name, config_name)
    print ('cli_file is', cli_file)


    child = pexpect.spawn('telnet {0} {1}'.format(gns3_ip, fetch_node_console(gns3_ip, project_name, node_name)))

    if node_type == 'voss':

        child.sendline('')
        child.sendline('logout')

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
        child.sendline('logout')
        child.close()

    elif node_type == 'exos':

        child.sendline('')
        child.sendline('logout')

        child.sendline('')
        child.expect('login: ')

        child.sendline('admin')

        child.expect('password: ')

        child.sendline('\n')

        for line in open(cli_file):
            cmd = line.rstrip('\n')
            print (cmd)
            child.sendline(cmd)

        child.sendline('save')
        child.expect('(y/N)')
        child.sendline('Y')
        child.sendline('logout')
        child.close()

def push_test(gns3_ip, project_name, node_name, node_type, test_group):

    vm_file = '/Users/yzeng/Documents/Gates/My Documents/Working In Progress/Extreme/GNS3/GNS3/scripts/test-vm.csv'
    print('starting', node_name, test_group)
    print('vm_file', vm_file)

    child = pexpect.spawn('telnet {0} {1}'.format(gns3_ip, fetch_node_console(gns3_ip, project_name, node_name)))

    if node_type == 'vpc':
        child.sendline('\n')
        child.expect('>')
        vm_name = node_name[2:] + '-Top'
        print ('vm_name', vm_name)
        ping_test(child, vm_file, vm_name, test_group)

    else:
        pass


def upgrade_sw(gns3_ip, project_name, sw_mgmt_ip, node_name, node_type, package_name):

#    working_dir = "/Users/yzeng/Documents/Gates/My Documents/Working In Progress/Extreme/GNS3/GNS3/scripts/5-nodes/"
    working_dir = "/Users/yzeng/Documents/Gates/My Documents/Working In Progress/Extreme/GNS3"
    ftp_user = "rwa"
    ftp_pass = "rwa"

    version_number = package_name.rsplit('.', 1)[0]

#    cli_file = working_dir + upgrade + ".txt"
#    print('starting', node_name, package_name)
#    print ('cli_file is', cli_file)

    pexpect.spawn('ftp -in -u ftp://{0}:{1}@{2}/{3} "{4}/{5}"'.format(ftp_user, ftp_pass, sw_mgmt_ip, package_name, working_dir, package_name),timeout=300).expect('Transfer complete')

    child = pexpect.spawn('telnet {0} {1}'.format(gns3_ip, fetch_node_console(gns3_ip, project_name, node_name)))

    if node_type == 'voss':

        child.sendline('')
        child.sendline('logout')

        child.sendline('')
        child.expect('Login: ')

        child.sendline('rwa')

        child.expect('Password: ')

        child.sendline('rwa')
        child.sendline('enable')

        child.sendline('software add {}'.format(package_name))
        child.sendline('software activate {}'.format(version_number))

        child.sendline('save config')
        child.expect('successful.')
        child.sendline('reset -y')



# relogin check activation status

        child.sendline('')
        child.sendline('logout')

        child.sendline('')
        child.expect('Login: ', timeout=240)

        child.sendline('rwa')

        child.expect('Password: ')

        child.sendline('rwa')
        child.sendline('enable')

        child.sendline('software activate {}'.format(version_number))
        child.expect('#')
        child.sendline('reset -y')

        # relogin check activation status
        '''
        child.sendline('')
        child.sendline('logout')

        child.sendline('')
        child.expect('Login: ', timeout=240)

        child.sendline('rwa')

        child.expect('Password: ')

        child.sendline('rwa')
        child.sendline('enable')

        child.sendline('software commit')
        child.expect('successful')

        child.sendline('')
        child.sendline('logout')
        '''

        child.close()

    elif node_type == 'exos':
        pass

def default_sw(gns3_ip, project_name, node_name, node_type):

#    working_dir = "/Users/yzeng/Documents/Gates/My Documents/Working In Progress/Extreme/GNS3/GNS3/scripts/5-nodes/"
#    working_dir = "/Users/yzeng/Documents/Gates/My Documents/Working In Progress/Extreme/GNS3/"
    ftp_user = "rwa"
    ftp_pass = "rwa"


    child = pexpect.spawn('telnet {0} {1}'.format(gns3_ip, fetch_node_console(gns3_ip, project_name, node_name)))

    if node_type == 'voss':

        child.sendline('')
        child.sendline('logout')

        child.sendline('')
        child.expect('Login: ')

        child.sendline('rwa')

        child.expect('Password: ')

        child.sendline('rwa')
        child.sendline('enable')
        child.expect('rwa connected via console port')
        child.sendline('delete config.cfg -y')

        child.writelines('reset -y\n\n\n')
        child.write('\n')

        child.close()


    elif node_type == 'exos':
        child.sendline('')

        child.sendline('logout')

        child.sendline('')
        child.expect('login: ')

        child.sendline('admin')

        child.expect('password: ')

        child.sendline('\n')

        child.sendline('unconfigure switch')
        child.expect('(y/N)')
        child.sendline('Y')
        child.close()

def cleanup_sw(gns3_ip, project_name, node_name, node_type, version):

#    cli_file = working_dir + upgrade + ".txt"
#    print('starting', node_name, package_name)
#    print ('cli_file is', cli_file)

    child = pexpect.spawn('telnet {0} {1}'.format(gns3_ip, fetch_node_console(gns3_ip, project_name, node_name)))

    if node_type == 'voss':

        child.sendline('')
        child.sendline('logout')

        child.sendline('')
        child.expect('Login: ')

        child.sendline('rwa')

        child.expect('Password: ')

        child.sendline('rwa')
        child.sendline('enable')

        child.sendline('software rem {}'.format(version))

        child.expect('#')

        child.sendline('del *.tgz -y')
        child.expect('(y/n) ?')

        child.sendline('y')

# relogin check activation status

        child.sendline('')
        child.sendline('logout')

        child.close()

    elif node_type == 'exos':
        pass


def capture_test(gns3_ip, project_name, node_name, node_type, config_name):
    cli_file = "/Users/yzeng/Documents/Gates/My Documents/Working In Progress/Extreme/GNS3/GNS3/scripts/5-nodes/" \
               + config_name + '/utest/' + node_name + ".txt"
    result_file = "/Users/yzeng/Documents/Gates/My Documents/Working In Progress/Extreme/GNS3/GNS3/scripts/5-nodes/" \
               + config_name + '/utest/results/' + node_name + ".txt"
    print('starting', node_name, config_name)
    print ('cli_file is', cli_file)

    # fout = open(result_file, 'w+')


    try:
        child = pexpect.spawn('telnet {0} {1}'.format(gns3_ip, fetch_node_console(gns3_ip, project_name, node_name)))
        # child.logfile = fout
        if node_type == 'voss':
            # login as rwa and enter enable mode
            child.sendline('')
            child.sendline('logout')
            child.sendline('')
            child.expect('Login: ')
            child.sendline('rwa')
            child.expect('Password: ')
            child.sendline('rwa')
            child.sendline('enable')

            child.expect('#')
            child.sendline('terminal more disable')

            # injecting all CLI commands
            for line in open(cli_file):
                cmd = line.rstrip('\n')
                print (cmd)
                child.sendline(cmd)

            # closing session
            child.sendline('logout')
            child.close()

            fout.close()

        elif node_type == 'exos':

            child.sendline('')
            child.sendline('logout')

            child.sendline('')
            child.expect('login: ')

            child.sendline('admin')

            child.expect('password: ')

            child.sendline('\n')

            for line in open(cli_file):
                cmd = line.rstrip('\n')
                print (cmd)
                child.sendline(cmd)

            child.sendline('save')
            child.expect('(y/N)')
            child.sendline('Y')
            child.sendline('logout')
            child.close()
    except:
        return
