import requests
from pprint import pprint
import telnetlib

host = '192.168.135.128'
port = 5009
user = "rwa\n"
password = "rwa"

tn = telnetlib.Telnet(host,port)
tn.write(("\n").encode('ascii'))


tn.read_until(b"Login: ")
tn.write(user.encode('ascii'))
tn.read_until(b"Password: ")
tn.write((password + "\n").encode('ascii'))

tn.read_until(b">")

command = "enable" + "\n"


tn.write(command.encode('ascii'))

tn.read_until(b"#")


command = "conf term" + "\n"

tn.write(command.encode('ascii'))

tn.read_until(b"#")

command = "snmp- name CMPa-50" + "\n"
tn.write(command.encode('ascii'))

tn.read_until(b"#")

tn.write("save config\n".encode('ascii'))

tn.read_until(b"#")

tn.close()

