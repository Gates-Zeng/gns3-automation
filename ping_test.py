import csv

def ping_test(child,vm_file, vm_name, test_group):

    prompt = '>'
    with open(vm_file, encoding= 'utf-8-sig' ) as File:
        data = list(csv.DictReader(File))
        for row in data:
            if row['Group'] == test_group and vm_name in row['VMs']:
                ip = row['IP_Addr']
                gw = row['GW_Addr']
                print(row['VMs'],ip, gw)
                child.sendline('ip {0}/24 {1}'.format(ip, gw))
                child.expect(prompt)
                child.sendline('ping {}'.format(gw))
                child.expect(prompt)

        for row in data:
            if row['Group'] == test_group and 'Top' in row['VMs']:
                ip = row['IP_Addr']
                print ('ping, ', ip)
                child.sendline('ping {} -c 5'.format(ip))
                child.expect(prompt)



