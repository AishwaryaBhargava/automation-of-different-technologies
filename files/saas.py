#!/usr/bin/python2

import commands as sp
import cgi

print("content-type: text/html")
print("\n")

cmd="sudo ansible-playbook saas.yml "
sp.getoutput(cmd)
print("software setup is successful")

