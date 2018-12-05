'''
Full flows

        1. get gns3 schema
        1.5 upgrade appliance (cannot be done through API)
            version
            hdd
        2. check current_project
            if non-exisitence then create
        3. check current topology
            topology xml
        4. upgrade appliance
        5. re-create topology
6. capturing tests results
    config to all nodes
    config to all vpcs
    collect test results
        run test commands
7. generate environment (show-tech)
     generate Jira
'''
import requests

class VossGns3Test:
    def __init__(self, compute_ip, project, voss_file, topology_file):
        self.gns3a = voss_file +'.gns3a'
        self.topology = topology_file
        self.project = project
        self.gns3vm = compute_ip

    def voss_upgrade(self):
        re = requests.get()