#!/usr/bin/python2

import commands as sp
import cgi

print("content-type: text/html")
print("\n")

cmd="sudo ansible-playbook caas.yml"
sp.getoutput(cmd)

print("setup succcessful")
print("now you can open in browser with ip 192.168.43.128 and port 3333")
