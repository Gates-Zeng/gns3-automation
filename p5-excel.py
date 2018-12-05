import csv

def ping_test(vm_file, vm_name, vlan):

    test_vm = vm_name + '-' + vlan
    with open(vm_file, encoding= 'utf-8-sig' ) as File:
        data = list(csv.DictReader(File))

        for row in data:
            if row['VMs'] == test_vm:
                ip = row['IP_Addr']
                gw = row['GW_Addr']
                group = row ['Group']
                print ('setting vm', ip, gw, group)


        for row in data:
            if row['Group'] == group:
                print ('pinging ip', row['IP_Addr'])



